
%Iniciar a captura de dados
PWM.B(1) = uicontrol(...
    'Style','pushbutton',...
    'Parent',PWM.ID,...'
    'string', 'Obter dados',...
    'Units','normalized',...
    'Position', [0.76 0.15 0.2 0.075],...
    'Visible','on','Enable','on',...
    'Callback','PWMCaptura','fontsize',9);

%Salvar os dados
PWM.B(2) = uicontrol(...
    'Style','pushbutton',...
    'Parent',PWM.ID,...
    'string', 'Salvar',...
    'Units','normalized',...
    'Position', [0.76 0.05 0.2 0.075],...
    'Visible','on','Enable','on',...
    'Callback','PWMescreverXY','fontsize',9);

%Entrada de dados: Número do jogador | PWM usado | Medida de número n
PWM.B(4) = uicontrol(PWM.ID,'style','popup','string',{'1','2','3'},'units','normalized','position',[0.05 0.69 0.2 0.075],'fontsize',09,'enable','on','Value',1);
PWM.B(5) = uicontrol(PWM.ID,'style','edit','string','1',  'units','normalized','position',[0.04 0.07 0.2 0.075],'horizontalalignment','center','fontsize',9);
PWM.B(6) = uicontrol(PWM.ID,'style','edit','string','50',  'units','normalized','position',[0.28 0.07 0.2 0.075],'horizontalalignment','center','fontsize',9);
PWM.B(7) = uicontrol(PWM.ID,'style','edit','string','50',  'units','normalized','position',[0.52 0.07 0.2 0.075],'horizontalalignment','center','fontsize',9);
PWM.B(8) = uicontrol(PWM.ID,'style','popup','string',{'Amarelo','Ciano'},'units','normalized','position',[0.05 0.50 0.2 0.075],'fontsize',09,'enable','on','Value',1);
PWM.B(9) = uicontrol(PWM.ID,'style','edit','string','5',  'units','normalized','position',[0.04 0.25 0.2 0.075],'horizontalalignment','center','fontsize',9);

%Textos
PWM.T(1) = uicontrol(PWM.ID,'style','text','string','Número do jogador'       ,'units','normalized','position',[0.05 0.78 0.2 0.05],'horizontalalignment','center','fontsize',9);
PWM.T(2) = uicontrol(PWM.ID,'style','text','string','Teste Número'       ,'units','normalized','position',[0.04 0.15 0.2 0.05],'horizontalalignment','center','fontsize',9);
PWM.T(3) = uicontrol(PWM.ID,'style','text','string','Potência Esquerda'       ,'units','normalized','position',[0.28 0.15 0.2 0.05],'horizontalalignment','center','fontsize',9);
PWM.T(4) = uicontrol(PWM.ID,'style','text','string','Potência Direita'       ,'units','normalized','position',[0.52 0.15 0.2 0.05],'horizontalalignment','center','fontsize',9);
%Indica o tempo de uma captura
PWM.T(5) = uicontrol(PWM.ID,'style','text','string','Tempo entre amostras: ' ,'units','normalized','position',[0.025 0 0.4 0.05],'horizontalalignment','center','fontsize',8);
%Indica o tempo total de amostragem
PWM.T(6) = uicontrol(PWM.ID,'style','text','string','Tempo de teste:'       ,'units','normalized','position',[0.405 0 0.4 0.05],'horizontalalignment','center','fontsize',8);
PWM.T(7) = uicontrol(PWM.ID,'style','text','string','Cor do teste'       ,'units','normalized','position',[0.05 0.59 0.2 0.05],'horizontalalignment','center','fontsize',9);
PWM.T(8) = uicontrol(PWM.ID,'style','text','string','Tempo de amostragem(s)'       ,'units','normalized','position',[0.04 0.33 0.2 0.06],'horizontalalignment','center','fontsize',9);

%Tela para mostrar segmentação

PWM.SegIm = subplot(1,1,1,'parent',PWM.ID,'Position',[0.3 0.36 0.6 0.6]); axis off
PWM.SegImOn = uicontrol(PWM.ID,'style','checkbox','string','Imagem','units','normalized','position',[0.1 0.9 0.12 0.1],'fontsize',9,'enable','on','Value',1);
