set(Campo.ID,'visible','off',...
    'Position',[0.4 1 0.6 1].*BDP.DimTela([3 2 3 4]) + [0 50 0 -80],...
    'OuterPosition',[0.4 1 0.6 1].*BDP.DimTela([3 2 3 4]) + [0 50 0 -80]);

% Habilitar captura de imagem e correlação dos pontos
set(Campo.Botoes(1:2),'enable','on')
CampoCapturarImagem