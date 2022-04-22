%Giro máximo para esquerda
    
COM.msg = ['B' 'D' 50 200 50 200 50 200 'P' 10]; % Valor real é -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
    
         set(BDP.status(2),'string','Pontência Direita: 50   Pontência Esquerda: 250')