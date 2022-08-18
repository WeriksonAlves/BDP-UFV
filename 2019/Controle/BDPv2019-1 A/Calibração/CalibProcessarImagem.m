
%% Determina a segmentação e exibe a imagem final da cor escolhida

% Converte a imagem atual de RGB para HSV [0,255]
% TESTAR PDI


Calib.Imagem.Atual = rgb2hsv(flipud(imresize(getsnapshot(Cam.Video),Cam.Redimensionar,'bicubic')));

% Determina o número da cor escolhida [R,O,Y,G,C,B,M,ALL]
for ii = 1:length(Calib.Cores)
    if Calib.Cores(ii).Value
        Calib.Imagem.Cor = ii;
        break
    end
end

% Se a opção escolhida não for a Total
if Calib.Imagem.Cor ~= 8
    
    % Habilita os Edits, os Sliders e o botão de Segmentar Pixels
    set(Calib.Edit,'enable','on')
    set(Calib.Slider,'enable','on')
    set(Calib.Botoes,'enable','on')
    
    % Atualiza os valores dos Edits e dos Sliders
    for ii = 1:6
        Calib.Edit(ii).String  = num2str(Calib.LimitesHSV(Calib.Imagem.Cor,ii));
        Calib.Slider(ii).Value = round(Calib.LimitesHSV(Calib.Imagem.Cor,ii));
    end
    
    % Atualizar cor dos Sliders
    set(Calib.Slider(1),'backgroundcolor',hsv2rgb([Calib.Slider(1).Value/360 1 1]))
    set(Calib.Slider(2),'backgroundcolor',hsv2rgb([Calib.Slider(2).Value/360 1 1]))
    
    for ii = 3:6
        set(Calib.Slider(ii),'backgroundcolor',[1 1 1]*Calib.Slider(ii).Value/100)
    end
    
    
    % Chama a função para segmentar uma cor individualmente
    CalibSegmentarCor
    
    
    % Se a opção escolhida for a Total
else
    % Altera os valores dos edits
    set(Calib.Edit(1),'string',0)
    set(Calib.Edit(2),'string',360)
    set(Calib.Edit(3),'string',0)
    set(Calib.Edit(4),'string',100)
    set(Calib.Edit(5),'string',0)
    set(Calib.Edit(6),'string',100)
    
    % Altera a cor de fundo e os valores dos sliders
    set(Calib.Slider(1),'backgroundcolor',[0 0 0],'value',0)
    set(Calib.Slider(2),'backgroundcolor',[1 1 1],'value',360)
    set(Calib.Slider(3),'backgroundcolor',[0 0 0],'value',0)
    set(Calib.Slider(4),'backgroundcolor',[1 1 1],'value',100)
    set(Calib.Slider(5),'backgroundcolor',[0 0 0],'value',0)
    set(Calib.Slider(6),'backgroundcolor',[1 1 1],'value',100)
    
    % Desabilita os edits, os sliders e o botão de Segmentar Pixels
    set(Calib.Edit,'enable','off')
    set(Calib.Slider,'enable','off')
    set(Calib.Botoes,'enable','off')
    
    % Chama a função para segmentar todas as cores
    
    CalibSegmentarTotal
    
end

% Exibe na tela a imagem final segmentada da cor escolhida

imshow(Calib.Imagem.Final,'Parent',Calib.Imagem.ID)


