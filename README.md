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

Agora temos um objeto do tipo Discipina! Podemos acessar suas informações da seguinte maneira:

```python
>>> disc.nome
'Eletromagnetismo'
>>> disc['nome']
'Eletromagnetismo'
>>> disc.instituto
'Instituto de Física'
>>> disc['instituto']
'Instituto de Física'
```

Utilize o método ``` .chaves() ``` para ver todos os outros atributos dessa classe

```python
>>> disc.chaves()
('instituto',
 'departamento',
 'codigo',
 'nome',
 'nome_ingles',
 'creditos_aula',
 'creditos_trabalho',
 'carga_horaria_total',
 'tipo',
 'ativacao',
 'desativacao',
 'objetivos',
 'programa_resumido',
 'programa',
 'avaliacao',
 'bibliografia',
 'requisitos',
 'oferecimento')
```

### Disciplina pelo nome

Se você optar encontrar uma disciplina pelo código

```python
>>> discs = client.disciplina_nome('Eletromagnetismo')
>>> discs.codigos_disciplinas()
('4300372',
 'PTC3213',
 'SEL0608',
 'PTC2313',
 'SEL0309',
 'LOM3205',
 '7600021',
 '5910150',
 '7600035',
 '7600036',
 '4300303',
 '4302303',
 '4300304',
 '4302304',
 '4300373',
 'PTC2310')
```

Para escolher uma disciplina, podemos selecionar o seu indície no objeto.

```python
>>> discs[0]
<jupiterweb.api.Disciplina object at 0x0000021754E971C0>
```

Assim é retornado um objeto do tipo Disciplina, o qual sabemos como utilizar.

Também é possível selecionar pelo código da disciplina:

```python
>>> discs.obter_disciplina('4300372')
<jupiterweb.api.Disciplina object at 0x0000021754E971C0>
```


## ✏ O que falta fazer?  

- Documentar a API.
- Função Calendário.

Se sentiu falta de alguma coisa? Tem alguma sugestão? Entre em contato comigo ou utilize das ferramentas do Github.
