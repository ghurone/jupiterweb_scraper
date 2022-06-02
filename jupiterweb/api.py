import requests
from bs4 import BeautifulSoup


def oferecimento_por_codigo(codigo:str):
    URL = 'https://uspdigital.usp.br/jupiterweb/obterTurma'
    req = requests.get(URL, params={'sgldis': codigo})
    
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        
        if msg:
            return [{'Erro': msg.text.strip()}]
        else: 
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
    else:
        raise requests.HTTPError(f'erro: {req.status_code}')
        

def requisitos_por_codigo(codigo:str):
    URL = 'https://uspdigital.usp.br/jupiterweb/listarCursosRequisitos'
    req = requests.get(URL, params={'coddis':codigo})
    
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        
        if msg:
            return [{'Erro': msg.text.strip()}]
        else:   
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
        
    else:
        raise requests.HTTPError(f'erro: {req.status_code}')
         

def buscar_disciplina_por_codigo(codigo:str) -> dict:
    URL = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina'
    req = requests.get(URL, params={'sgldis': codigo})
    
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        if msg:
            raise ValueError(msg.text.strip())
        
        tabela_bruta = soup.find('form', attrs={'name':'form1'}).find_all('span')
        itens = ['Instituto', 'Departamento', 'Nome disciplina', 'Nome inglês']
        conteudo = {}
        
        i = 0
        for row in tabela_bruta:
            cls = row.attrs.get('class')[0]
            
            if cls == 'txt_arial_8pt_black':
                chave = row.text.strip().replace(':', '')
                 
                if 'Desativação' in chave and len(chave) > 11:
                    chave_temp = 'Desativação'
                    conteudo[chave_temp] = chave.split(' ')[1].strip()
                else:
                    conteudo[chave] = ''
                
                if chave == 'Docente(s) Responsável(eis)':
                    conteudo[chave] = []
                
            elif cls == 'txt_arial_8pt_gray':
                texto = row.text.strip().replace('\n','').replace('\t', '').replace('\r', '').replace('\xa0', ' ')
                
                if texto:
                    if chave == 'Docente(s) Responsável(eis)':
                        conteudo[chave].append(texto)
                    else:
                        conteudo[chave] += texto
                        
            elif cls == 'txt_arial_10pt_black':
                conteudo[itens[i]] = row.text.strip() 
                i += 1
                
        disc = Disciplina(conteudo)
        
        if disc.requisitos == '':
            disc.requisitos = requisitos_por_codigo(codigo)
        
        if disc.oferecimento == '':
            disc.oferecimento = oferecimento_por_codigo(codigo)
        
        return disc
            
    else:
        raise requests.HTTPError(f'erro: {req.status_code}')
    
    
def buscar_disciplina_por_nome(nome:str):
    nome = nome.strip()
    
    if len(nome) > 30:
        raise ValueError('A sua busca é muito grande')
    
    URL = 'https://uspdigital.usp.br/jupiterweb/obterDisciplina'
    
    req = requests.get(URL, params={'nomdis':nome})
    
    if req.status_code == 200:
        soup = BeautifulSoup(req.text, 'lxml')
        
        msg = soup.find('div', attrs={'id':'web_mensagem'})
        if msg:
            raise ValueError(msg.text.strip())
        
        tabela_bruta = soup.find(lambda tag:tag.name == "table" and len(tag.attrs) == 2).find_all('a')
        disc = []
        
        for row in tabela_bruta:
            disc.append((row.attrs['href'][23:30], row.text))
            
        return Disciplinas(disc)
        
    else:
        raise requests.HTTPError(f'erro: {req.status_code}')
    
    
class Disciplina:
    def __init__(self, dicio:dict) -> None:
        self.sigla, self.nome = dicio['Nome disciplina'][12:19], dicio['Nome disciplina'][22:]
        self.departamento = dicio['Departamento']
        self.instituto = dicio['Instituto']
        self.nome_en = dicio['Nome inglês']
        
        self.cred_aula = dicio['Créditos Aula']
        self.cred_trab = dicio['Créditos Trabalho']
        self.carga_horaria = dicio['Carga Horária Total']
        self.tipo = dicio['Tipo']
        self.data_ativação = dicio['Ativação']
        self.data_desativação = dicio['Desativação']
        
        try:
            self.docentes = dicio['Docente(s) Responsável(eis)']
        except KeyError:
            self.docentes = []
        
        self.objetivos = dicio['Objetivos']
        self.programa_resumido = dicio['Programa Resumido']
        self.programa = dicio['Programa']
        self.avaliação = {'Método': dicio['Método'], 'Critério': dicio['Critério'],
                          'Norma de Recuperação': dicio['Norma de Recuperação']}
        self.bibliografia = dicio['Bibliografia']

        try:
            self.requisitos = dicio['Requisitos']
        except KeyError:
            self.requisitos = ''
            
        self.oferecimento = ''
        
        
class Disciplinas:
    def __init__(self, lista:list) -> None:
        self.lista = lista
    
    def __str__(self) -> str:
        return str(self.lista)
    
    def __repr__(self) -> str:
        return repr(self.lista)
    
    def __getitem__(self, item):
        return buscar_disciplina_por_codigo(self.lista[item][0])