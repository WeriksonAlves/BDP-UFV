%Roda apenas o lado esquerdo
    
COM.msg = ['B' 'D' 150 200 150 200 150 200 'P' 10]; % Valor real � -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
    
 set(BDP.status(2),'string','Pont�ncia Direita: 150   Pont�ncia Esquerda: 250')