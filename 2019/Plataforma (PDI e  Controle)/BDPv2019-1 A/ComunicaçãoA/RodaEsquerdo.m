%Roda apenas o lado esquerdo
    
COM.msg = ['B' 'D' 150 200 150 200 150 200 'P' 10]; % Valor real é -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
    
 set(BDP.status(2),'string','Pontência Direita: 150   Pontência Esquerda: 250')