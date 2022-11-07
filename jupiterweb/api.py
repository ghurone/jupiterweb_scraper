from unicodedata import normalize

import requests
from bs4 import BeautifulSoup

import jupiterweb.exceptions as exc


class Disciplina:
    def __init__(self, dicio:dict) -> None:
        self._dicio = {}
        
        for key, value in dicio.items():
            key = normalize('NFD', key).encode('ascii', "ignore")
            key = key.decode('utf8').replace(' ', '_').lower()
            self._dicio[key] = value
        
    def __str__(self) -> str:
        return str(self._dicio)

    def __getattr__(self, _name: str):
        return self[_name]
    
    def __getitem__(self, _name:str):
        if _name in self.chaves():
            return self._dicio[_name]
        raise exc.DisciplinaError('Essa chave não existe!')
    
    def __setitem__(self, *args):
        raise exc.DisciplinaError('As Disciplinas são imutáveis.')
    
    def __iter__(self):
        return iter(self._dicio)
    
    def chaves(self):
        return tuple(self._dicio.keys())
    
    def itens(self):
        return self._dicio.items()
    
    
class GrupoDisciplinas:
    def __init__(self, lista:tuple[tuple[str,str]]) -> None:
        self._lista = lista
        self._dicio = dict(elem for elem in lista)
        
        self._client = JupiterWeb()
        
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('O indíce precisa ser um número inteiro.')
        
        if key > len(self._lista) - 1:
            raise IndexError('Indíce fora do interválo.')
        
        return self._client.disciplina_codigo(self._lista[key][0])

    def __setitem__(self, *args):
        raise exc.GrupoDisciplinaError('O objeto `GrupoDisciplinas` é imutável.')
    
    def __str__(self) -> str:
        return str(self._lista)
    
    def __repr__(self) -> str:
        return str(self)
    
    def __len__(self) -> int:
        return len(self._lista)
    
    def codigos_disciplinas(self):
        return tuple(self._dicio.keys())
    
    def obter_disciplina(self, codigo):
        codigo = str(codigo)
        if not codigo in self.codigos_disciplinas():
            raise exc.GrupoDisciplinaError('Esse código não está no grupo.')
        
        index = self.codigos_disciplinas().index(codigo)
        return self[index]


class JupiterWeb:
    
    def disciplina_codigo(self, codigo: str or int) -> Disciplina:
        
        if not isinstance(codigo, (int, str)):
            raise TypeError('O código precisa ser do tipo `int` ou `str`')
        
        URL = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina'
        req = requests.get(URL, params={'sgldis': codigo})
        req.raise_for_status()
        
        soup = BeautifulSoup(req.text, 'lxml')
        
        self._check_erro(soup)
        
        tabela_bruta = soup.find('form', attrs={'name':'form1'}).find_all('span')
        itens = ['Instituto', 'Departamento', 'Disciplina', 'Nome ingles']
        conteudo = {}
        
        i = 0
        for row in tabela_bruta:
            cls = row.attrs.get('class')[0]
            texto = ' '.join(row.text.split())
            
            if cls == 'txt_arial_8pt_black':
                chave = texto.replace(':', "")
                    
                if 'Desativação' in chave and len(chave) > 11:
                    chave_temp = 'Desativação'
                    conteudo[chave_temp] = chave.split(' ')[1].strip()
                
                elif chave == 'Docente(s) Responsável(eis)':
                    conteudo['Docentes'] = []
                    
                else:
                    conteudo[chave] = ''
                
            elif cls == 'txt_arial_8pt_gray':
                if texto:
                    if chave == 'Docente(s) Responsável(eis)':
                        conteudo['Docentes'].append(texto)
                    else:
                        conteudo[chave] += texto
                        
            elif cls == 'txt_arial_10pt_black':
                if i != 2:
                    conteudo[itens[i]] = texto
                else:
                    code, nome = texto.split('-', 1)
                    code = code.split(':', 1)[-1]
                    conteudo['Codigo'] = code.strip()
                    conteudo['Nome'] = nome.strip()
                    
                i += 1
        
        conteudo['Avaliacao'] = {'metodo': conteudo['Método'], 'criterio': conteudo['Critério'],
                          'norma_de_recuperacao': conteudo['Norma de Recuperação']}
        
        del conteudo['Método']
        del conteudo['Norma de Recuperação']
        del conteudo['Critério']
        
        conteudo['Requisitos'] = self._requisitos_por_codigo(codigo)
        conteudo['Oferecimento'] = self._oferecimento_por_codigo(codigo)
        
        return Disciplina(conteudo) 

    def disciplina_nome(self, nome:str) -> GrupoDisciplinas:
   
        if not isinstance(nome, str):
            raise TypeError('O nome da disciplina precisa ser do tipo `str`')
        
        nome = nome.strip()
        
        URL = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina'
        req = requests.get(URL, params={'nomdis':nome})
        req.raise_for_status() 
        
        soup = BeautifulSoup(req.text, 'lxml')
        
        # Se tiver mensagem de erro
        self._check_erro(soup)
        
        tabela_bruta = soup.find(lambda tag:tag.name == "table" and len(tag.attrs) == 2).find_all('a')
        disc = tuple((row.attrs['href'][23:30], row.text) for row in tabela_bruta)
            
        return GrupoDisciplinas(disc)
    
    def _oferecimento_por_codigo(self, codigo: str or int) -> list[dict]:

        if not isinstance(codigo, (int, str)):
            raise TypeError('O código precisa ser do tipo `int` ou `str`')
        
        URL = 'https://uspdigital.usp.br/jupiterweb/obterTurma'
        req = requests.get(URL, params={'sgldis': codigo})
        req.raise_for_status()
        
        soup = BeautifulSoup(req.text, 'lxml')
        
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        if msg:
            return [{'Erro': msg.text.strip()}]

        tabelas_brutas = soup.find_all('div', 
                                    attrs={'style': 'border: 2px solid #658CCF; padding: 5px; border-radius: 5px;'})
        tabelas = []
        
        for div in tabelas_brutas:
            tabela_1 = div.find('table', attrs={'cellspacing':'2'})
            tabela_2 = div.find('table', attrs={'cellspacing':'1'})
            tabela_3 = div.find('table', attrs={'align':'center'})
            
            t_1 = {}
            for font in tabela_1.find_all('font'):
                if font['color'] == '#000000':
                    chave = font.text
                    chave = " ".join(chave.split())
                    t_1[chave] = ''
                    
                elif font['color'] == '#666666':
                    texto = font.text.strip()
                    texto = " ".join(texto.split())
                    
                    t_1[chave] += texto
            
            t_2 = {'Horários': []}
            for row in tabela_2.find_all('tr'):
                if row.font['color'] == '#666666':
                    texto = row.text
                    texto = " ".join(texto.split())
                    
                    t_2['Horários'].append({'Horário':texto[:15], 'Prof(a)':texto[16:]})

            t_3 = {'Tipo':{}}
            for row in tabela_3.find_all('tr'):
                try:
                    row['bgcolor']
                except KeyError:
                    texto = row.text
                    texto = " ".join(texto.split())     
                    
                    texto_split = texto.split(' ')
                        
                    if row.font['color'] == '#000000':
                        
                        if len(texto_split) == 5:
                            chave = texto_split[0]
                        else:
                            chave = texto_split[0] + ' ' + texto_split[1]
                            
                        t_3['Tipo'][chave] = [{'Curso':'Total','Vagas':texto_split[-4],'Inscritos':texto_split[-3],
                                                'Pendentes':texto_split[-2], 'Matriculados':texto_split[-1]}]
                                        
                    else:                            
                        curso = ' '.join(texto_split[:-4])
                        t_3['Tipo'][chave].append({'Curso':curso,'Vagas':texto_split[-4],'Inscritos':texto_split[-3],
                                                'Pendentes':texto_split[-2], 'Matriculados':texto_split[-1]})
                                            
            tabelas.append({**t_1, **t_2, **t_3})
        
        return tabelas

    def _requisitos_por_codigo(self, codigo: str or int) -> list[dict]:
        
        if not isinstance(codigo, (int, str)):
            raise TypeError('O código precisa ser do tipo `int` ou `str`')
        
        URL = 'https://uspdigital.usp.br/jupiterweb/listarCursosRequisitos'
        req = requests.get(URL, params={'coddis':codigo})
        req.raise_for_status()
        
        soup = BeautifulSoup(req.text, 'lxml')
        
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        if msg:
            return [{'Erro': msg.text.strip()}]

        tabela_bruta = soup.find('form', attrs={'name':'form1'}).find('table',attrs={'cellspacing':'2'}).find_all('td')
        tabela = []
        
        i = -1
        for row in tabela_bruta:
            if row.font and row.font['color'] == '#FFFFFF':
                chave = row.font.text
                chave = " ".join(chave.split())
                tabela.append({'Curso': chave[7:], 'Disciplinas':[]})
                
                i += 1
                
            elif not row.div:
                texto = row.text.strip()
                
                if len(texto) > 7:
                    texto = " ".join(texto.split())
                    tabela[i]['Disciplinas'].append({'Sigla': texto[:7], 'Nome':texto[10:]})
                
        return tabela

    @staticmethod
    def _check_erro(soup:BeautifulSoup) -> None:
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        if msg:
            raise exc.JupiterWebMsgError(msg.text.strip())