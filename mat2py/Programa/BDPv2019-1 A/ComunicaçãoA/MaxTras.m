%M�ximo para tr�s
    
COM.msg = ['B' 'D' 50 50 50 50 50 50 'P' 10]; % Valor real � -150
    for i = 1:500
    
    %fprintf(COM.Porta,COM.msg);

    fwrite(COM.Porta,COM.msg,'char');

    end
  
    set(BDP.status(2),'string','Pont�ncia Direita: 50   Pont�ncia Esquerda: 50')