# jupiterweb-scraper

![PyPI](https://img.shields.io/pypi/v/jupiterweb?label=Vers%C3%A3o&style=flat-square)

Um scraper de disciplinas do [jupiterweb](https://uspdigital.usp.br/jupiterweb/). 

## 📝 Requisitos 

Antes de instalar você precisa ter os seguintes pacotes:

```python
requests>=2.26.0
beautifulsoup4>=4.10.0
lxml>=4.6.3
```

Não se preocupe tanto com a versão, pois não utilizei nada de específico dos pacotes.

## ⚙ Como instalar 

É bem fácil de instalar, caso você já tenha o pip instalado e configurado é só utilizar o comando de instalação

```bash
pip install jupiterweb
```

## 🧙‍♂️ Guia rápido 

No momento, o scraper só possui duas funcionalidades, buscar disciplinas pelo código ou pelo nome. E podem ser importados da seguinte maneira

```python
>>> from jupiterweb import buscar_disciplina_por_codigo, buscar_disciplina_por_nome
```

### Disciplna pelo codigo

Se você optar encontrar uma disciplina pelo código

```python
>>> disc = buscar_disciplina_por_codigo('4300372')
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

Para saber mais atributos, use o seguinte comando:

```python
>>> disc.__dict__
...
```

### Disciplina pelo nome

Se você optar encontrar uma disciplina pelo código

```python
>>> discs = buscar_disciplina_por_nome('Eletromagnetismo')
>>> discs
discs
[('4300372', 'Eletromagnetismo'), ('PTC3213', 'Eletromagnetismo'), ('SEL0608', 'Eletromagnetismo'), ('PTC2313', 'Eletromagnetismo'), ('SEL0309', 'Eletromagnetismo'), ('LOM3205', 'Eletromagnetismo'), ('7600021', 'Eletromagnetismo'), ('5910150', 'Eletromagnetismo'), ('7600035', 'Eletromagnetismo Avançado'), ('7600036', 'Eletromagnetismo Computacional'), ('4300303', 'Eletromagnetismo I'), ('4302303', 'Eletromagnetismo I'), ('4300304', 'Eletromagnetismo II'), ('4302304', 'Eletromagnetismo II'), ('4300373', 'Laboratório de Eletromagnetismo'), ('PTC2310', 'Noções de Ondas e Eletromagnetismo')]
```

Nesse caso ele mostra uma lista de tuplas. Ai você escolhe a disciplina pelo indice.

```python
>>> discs[0]
<jupiterweb.api.Disciplina object at 0x0000021754E971C0>
```

E sabemos manipular esse tipo de objeto, já que foi visto no outro tutotrial, é só manipular da mesma maneira.

## ✏ O que falta fazer?  

- Calendário

Se sentiu falta de alguma coisa, entra em contato comigo, no meu perfil você consegue achar maneiras de se comunicar comigo!
