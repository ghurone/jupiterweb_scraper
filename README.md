# JúpiterWeb Scraper

![PyPI - Python Version](https://img.shields.io/badge/python-%3E%3D%203.8%20-blue?style=flat-square)

![PyPI](https://img.shields.io/pypi/v/jupiterweb?label=Versão&style=flat-square)

Um scraper de disciplinas do [jupiterweb](https://uspdigital.usp.br/jupiterweb/). 

## ⚙ Como instalar 

Caso você já tenha o pip instalado e configurado é só utilizar o comando de instalação:

```bash
pip install jupiterweb
```

Se o pip não estiver configurado, pode tentar instalar da seguinte maneira:

```bash
python -m pip install jupiterweb
```

Se nenhum dos comandos acima funcionar, pesquise em como con

## 🧙‍♂️ Guia rápido 

No momento, o scraper só possui duas funcionalidades, buscar disciplinas pelo código ou pelo nome. E podem ser importados da seguinte maneira

```python
>>> from jupiterweb import JupiterWeb
>>> client = JupiterWeb()
```

### Disciplna pelo codigo

Se você optar encontrar uma disciplina pelo código

```python
>>> disc = client.disciplina_codigo('4300372')
>>> disc 
<jupiterweb.api.Disciplina object at 0x000001B433080D00>
```

Agora temos um objeto do tipo Discipina, vou mostrar algums atributos que ele possui.

```python
>>> disc.nome
'Eletromagnetismo'
>>> disc.instituto
'Instituto de Física'
>>> disc.cred_trab
'0'
>>> disc.cred_aula
'4'
>>> disc.objetivos
'ok'
>>> disc.requisitos
[{'Curso': '43031 Física Licenciatura (diurno) - Período ideal: 6', 'Disciplinas': [{'Sigla': '4300160', 'Nome': 'Ótica'}, {'Sigla': '4300271', 'Nome': 'Eletricidade e Magnetismo II'}, {'Sigla': 'MAT0105', 'Nome': 'Geometria Analítica'}, {'Sigla': 'MAT2351', 'Nome': 'Cálculo para Funções de Várias Variáveis I'}]}, {'Curso': '43031 Física Licenciatura (noturno) - Período ideal: 6', 'Disciplinas': [{'Sigla': '4300160', 'Nome': 'Ótica'}, {'Sigla': '4300271', 'Nome': 'Eletricidade e Magnetismo II'}, {'Sigla': 'MAT0105', 'Nome': 'Geometria Analítica'}, {'Sigla': 'MAT2351', 'Nome': 'Cálculo para Funções de Várias Variáveis I'}]}]
```

Para saber mais atributos da classe:

```python
>>> disc.__dict__.keys()
dict_keys(['sigla', 'nome', 'departamento', 'instituto', 'nome_en', 'cred_aula', 'cred_trab', 'carga_horaria', 'tipo', 'data_ativação', 'data_desativação', 'docentes', 'objetivos', 'programa_resumido', 'programa', 'avaliação', 'bibliografia', 'requisitos', 'oferecimento'])
```

### Disciplina pelo nome

Se você optar encontrar uma disciplina pelo código

```python
>>> discs = client.disciplina_nome('Eletromagnetismo')
>>> discs
discs
(('4300372', 'Eletromagnetismo'), ('PTC3213', 'Eletromagnetismo'), ('SEL0608', 'Eletromagnetismo'), ('PTC2313', 'Eletromagnetismo'), ('SEL0309', 'Eletromagnetismo'), ('LOM3205', 'Eletromagnetismo'), ('7600021', 'Eletromagnetismo'), ('5910150', 'Eletromagnetismnto'), ('7600035', 'Eletromagnetismo Avançado'), ('7600036', 'Eletromagnetismo Computacional'), ('4300303', 'Eletromagnetismo I'), ('4302303', 'Eletromagnetismo I'), ('4300304', 'Eletromagnetismo II'), ('4302304', 'Eletromagnetismo II'), ('4300373', 'Laboratório de Eletromagnetismo'), ('PTC2310', 'Noções de Ondas e Eletromagnetismo'))
```

Nesse caso ele mostra uma lista de tuplas. Então para escolher uma disciplina, basta selecionar o seu indicie no objeto.

```python
>>> discs[0]
<jupiterweb.api.Disciplina object at 0x0000021754E971C0>
```

## ✏ O que falta fazer?  

- Calendário

Se sentiu falta de alguma coisa, entra em contato comigo, no meu perfil você consegue achar maneiras de se comunicar comigo!
