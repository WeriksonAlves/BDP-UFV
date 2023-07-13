% Carregar limites HSV de calibra��o
set(BDP.status(1),'String','Leitura calibra��o')

if exist('LimitesHSV.mat','file') == 2    
    load('LimitesHSV.mat');
    Calib.LimitesHSV = LimitesHSV;
    set(BDP.status(2),'String','Limites HSV: Sucessso!!!')
else
    % Dados iniciais de calibra��o
    Calib.LimitesHSV = [...
        330 015 000 100 000 100;
        015 045 000 100 000 100;
        045 090 000 100 000 100;
        090 150 000 100 000 100;
        150 210 000 100 000 100;
        210 270 000 100 000 100;
        270 330 000 100 000 100];
    set(BDP.status(2),'String','Limites HSV: default')
end
PDI.LimitesHSV = Calib.LimitesHSV;

% Carregar transforma��o projetiva
if exist('TransfProjectiva.mat','file') == 2
    load('TransfProjectiva.mat');
    PDI.T = TransfProjectiva;
    set(BDP.status(2),'String',[get(BDP.status(2),'String') 10 'Transforma��o Projectiva: Sucessso!!!'])
else    
    set(BDP.status(2),'String',[get(BDP.status(2),'String') 10 'Transforma��o Projectiva: default'])
end


