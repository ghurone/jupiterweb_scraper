# jupiterweb-scraper

Um scraper de disciplinas do [jupiterweb](https://uspdigital.usp.br/jupiterweb/). 

## 📝 Requisitos 

Antes de instalar você precisa ter os seguintes pacotes:

```python
requests==2.26.0
beautifulsoup4==4.10.0
lxml==4.6.3
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
```

Para saber mais atributos, use o seguinte comando:

```python
>>> disc.__dict__
{'sigla': '4300372', 'nome': 'Eletromagnetismo', 'departamento': 'Disciplinas Interdepartamentais do Instituto de Física', 'instituto': 'Instituto de Física', 'nome_en': 'Electromagnetism', 'cred_aula': '4', 'cred_trab': '0', 'carga_horaria': '60 h', 'tipo': 'Semestral', 'data_ativação': '01/01/2010', 'data_desativação': '', 'docentes': [], 'objetivos': 'ok', 'programa_resumido': '', 'programa': 'Interação elétrica. Energia no campo, o dipolo elétrico. Interação magnética. Movimento de uma carga em um campo magnético. Interação magnética entre correntes e entre cargas. Campos eletromagnéticos estáticos na matéria. Polarização. A lei de Ampère na forma diferencial. Ondas eletromagnéticas. Energia e quantidade de movimento de uma onda eletromagnética. Radiação de dipolo. Radiação da carga acelerada. Campos eletromagnéticos dependentes do tempo. As leis de Maxwell em forma diferencial. Reflexão, refração e polarização. Interferência. Cavidades ressonantes. Guias de ondas. Difração.', 'avaliação': {'Método': 'ok', 'Critério': 'ok', 'Norma de Recuperação': 'com 2a avaliação'}, 'bibliografia': '.'}
```

### Disciplna pelo nome

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

## ✏ Falta fazer  

- Mostrar os requisitos das disciplinas
- Mostrar o oferecimento das disciplinas
- Calendário

Se sentiu falta de alguma coisa, entra em contato comigo, no meu perfil você consegue achar maneiras de se comunicar comigo!