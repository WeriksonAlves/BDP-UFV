%Roda apenas o lado direito
    
COM.msg = ['B' 'D' 250 150 250 150  250 150 'P' 10]; % Valor real é -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
    
     set(BDP.status(2),'string','Pontência Direita: 250   Pontência Esquerda: 150')