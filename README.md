# Madalena

Madalena é um projeto composto por uma aplicação chamada Funnel, que é API RestFul que serve como ponto de entrada para uma outra aplicação chamada Resizer, que se trata de um redimensionador de imagens feito com Tasks do Celery.

O escopo e modelagem de suas aplicações foi trabalhado de maneira a ser plugável, tentando ao máximo não ter nenhum tipo de acoplamento, para que possam inclusive ser utilizada em outros projetos.

### Funcionamento da Madalena

![Fluxograma Madalena](https://github.com/Dhanielr/madalena/blob/master/docs_imgs/Madalena.png)

## Funnel - API RestFul

A aplicação __Funnel__ é uma API RestFul criada a partir do [Django Rest Framework](https://www.django-rest-framework.org/), utilizando-se atualmente de um único verbo HTTP, o _POST_.

### Utilizando a API RestFul

Como utilizaremos o verbo POST para enviar uma *imagem* e outros parâmetros opcionais pela API, precisamos passá-los via _form-data_, que se encontra no corpo da requisição.

Parâmetros:


| Parâmetro               | Tipo             | Valor Padrão | Descrição                                                                                                          |
|-------------------------|------------------|--------------|--------------------------------------------------------------------------------------------------------------------|
| **image** *Obrigatório* | ImageFile        | None         | Parâmetro para definir a imagem que será redimensionada.                                                        |
| **width** *Opcional*    | Positive Integer | 384          | Parâmetro para definir a largura desejada na imagem redimensionada.                                         |
| **height** *Opcional*   | Positive Integer | 384          | Parâmetro para definir a altura desejada na imagem redimensionada.                                          |
| **crop** *Opcional*     | Boolean          | true         | Parâmetro para definir se a imagem pode ser cortada no momento do redimensionamento para manter proporcionalidade. |


## Resizer - Redimensionador de imagens 

A aplicação __Resizer__ trata-se de um *redimensionador de imagens*, utilizando-se das libs [Pillow](https://pypi.org/project/Pillow/) e [python-resize-image](https://pypi.org/project/python-resize-image/). 

## Instalação

A instalação é bem simples, detalharei abaixo os passos:

* Se desejar, faça um fork desse projeto caso queira alterá-lo. Clique no botão de **Fork** mais acima nessa mesma página.

* Faça um clone do repositório, se você tiver feito o *Fork* coloque a sua referência *ssh* no lugar da descrita abaixo:


        git clone git@github.com:Dhanielr/madalena.git 


* Após ter o repositório localmente, é importante que o mesmo ambiente do repositório já possua o [Docker](https://docs.docker.com/engine/install/), se não for esse o caso, basta clicar [aqui](https://docs.docker.com/engine/install/)  para instalar.

* É importante citar que o serviço do container rodará na porta **8020**, caso deseje mudar isso, altere os locais que possuirem *8020* nso arquivos *nginx.default* e *Dockerfile* e no comando do *docker run* logo a seguir.

* Tendo agora o ambiente com o Docker instalado e o repositório baixado localmente, acesse o repositório e rode o seguinte comando, para que seja criada a imagem para o nosso container:


        cd madalena
        sudo docker build -t madalena .

* Após a criação da imagem do docker com sucesso, basta agora rodar o container. Estou incluindo no comando parâmetros para que seja criado um usuário **admin** no painel *admin do Django*, para visualizer melhor as imagens que foram recebidas pela API e as redimensionadas.

    **Acesso:** *localhost:8020/admin*

    **Usuário:** admin
    
    **Senha:** 321mudar

        sudo docker run -it -p 8020:8020 -e DJANGO_SUPERUSER_USERNAME=admin -e DJANGO_SUPERUSER_PASSWORD=321mudar -e DJANGO_SUPERUSER_EMAIL=admin@example.com madalena

* Feito isso, nosso container Docker estará criado e rodando, bastando agora que o *celery* seja iniciado, para isso, precisamos acessar um *shell* do nosso container.

        sudo docker exec -it CONTAINER_ID /bin/bash

* Já no bash do nosso container, acesse a pasta */opt/app/madalena/* e execute a chamada do celery.

        celery -A madalena worker --loglevel=info

* Agora basta fazer seus envios para a url *localhost:8020/funnel* e verá a no seu *terminal do celery*, a recepção das tasks e no *terminal do docker run* as requisições http. 

:)
## Observações

Estou utilizando o [celery](http://www.celeryproject.org/) em conjunto com [redis](https://redis.io/) como *broker*, que está rodando em uma aplicação gratuita no [heroku](https://www.heroku.com/). 

A url da mesma já se encontra configurada no *madalena/settings.py*. Caso deseje rodar com uma própia instância do redis ou com outro broker fique a vontade para alterar no projeto.

## Considerações Finais

Essa aplicação é um *software livre* e seu desenvolvedor encoraja as práticas de DevOps.

O nome do projeto veio de uma dog muito fofa, que tenho muita vontade de conhecer pessoalmente. c:

### Referências

* [Docker](https://www.docker.com/)
* [Celery](http://www.celeryproject.org/)
* [Django](https://www.djangoproject.com/) 
* [Django REST framework](https://www.django-rest-framework.org/)
* [Redis](https://redis.io/)
* [Heroku](https://www.heroku.com/)

