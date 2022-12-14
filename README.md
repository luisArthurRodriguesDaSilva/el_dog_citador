<div align="center" >
  <h1 align="center"> dog das citações </h1>
 <img width=500 src="https://pbs.twimg.com/profile_images/1485962078733144066/yl74cBsn_400x400.jpg">
</div>
<hr />
  <p lang="pt" dir="ltr">
    O dog das citações, mas conhecido como <a href="https://twitter.com/el_dog_citador" >@el_dog_citador</a>, funciona através de uma lista de autores enviados pelos seguidores<p>
 <p>A cada dia são sorteados 5 desses autores e deles são sorteadas as citações</p>
    <p>Para adicionar um nome nessa lista de sorteio um seguidor deve mandar uma mensagem na dm com seguinte modelo</p>
  <h5>Autor: nome do autor</h5>
    <h4> Observe os exemplos a seguir: </h4>
  <div>                                                           
    <img width = 333 src="https://pbs.twimg.com/media/FPWdca7WUAQWZr9?format=jpg&name=360x360">
    <img width = 333 src="https://pbs.twimg.com/media/FPWdcoTWQAc2tsD?format=jpg&name=small">   
  </div>
<hr>
<div>
  <h1 >exemplos de twets:</h1>
  
  <img width = 800 src="https://pbs.twimg.com/media/FP8ZqaCXMAMw9s1?format=jpg&name=small">
  <img width = 800 src="https://pbs.twimg.com/media/FP8ZqEwXwAIaZ89?format=jpg&name=small">
  <img width = 800 src="https://pbs.twimg.com/media/FP8ZqPqXsAMDu3s?format=jpg&name=small">
</div>
<hr width=32%>

<h1>Diagrama do funcionamento</h1>

```mermaid
graph LR
exec((exec))
B(dm)
C(trending)
D(autor)
E(random)
a(string do autor)
A(array de strings do autor)
S(sortear citação do autor)
v(verificar a possibilidade da citação)
fp(foi possivel)
nfp(não foi possivel)
p{publicar}

exec --> E
exec --> D
exec --> B
exec --> C
B --> A
C --> A 
D --> a
E --> a
a --> S
A --> S
S --> v
v --> fp
v --> nfp
nfp --> S
fp --> p
```

<br />
<div align ="center">
  <a  href="https://twitter.com/el_dog_citador">
    clique aqui para ser redirecionado ao perfil
  </a>
</div>
