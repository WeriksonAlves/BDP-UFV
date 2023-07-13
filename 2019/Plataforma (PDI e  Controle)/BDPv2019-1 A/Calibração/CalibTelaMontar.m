%% Inicia a tela de calibração de cores

% Inicia e modifica os parâmetros da tela de calibração e chama a função FecharCalibracao para fechar

% ==============================================
% Segmentação de cores
Calib.Painel(1) = uipanel(Calib.ID,...
    'Title','Segmentação',...
    'units','normalized',...
    'position',[0.0 0.9 1 0.1]);

% Cria o espaço para o grupo de botões de cores
Calib.CoresG = uibuttongroup(Calib.Painel(1),'units','normalized','position',[0 0 1 1],'selectionchangedfcn','CalibProcessarImagem');

% Cria um botão para cada cor e marca a opção total como padrão
Calib.Cores(1) = uicontrol(Calib.CoresG,'style','radiobutton','string','Vermelho','units','normalized','position',[0/8 0 1/8 1],'backgroundcolor',[0.8 0.0 0.0],'fontsize',09);
Calib.Cores(2) = uicontrol(Calib.CoresG,'style','radiobutton','string','Laranja' ,'units','normalized','position',[1/8 0 1/8 1],'backgroundcolor',[0.8 0.4 0.0],'fontsize',09);
Calib.Cores(3) = uicontrol(Calib.CoresG,'style','radiobutton','string','Amarelo' ,'units','normalized','position',[2/8 0 1/8 1],'backgroundcolor',[0.8 0.8 0.0],'fontsize',09);
Calib.Cores(4) = uicontrol(Calib.CoresG,'style','radiobutton','string','Verde'   ,'units','normalized','position',[3/8 0 1/8 1],'backgroundcolor',[0.0 0.8 0.0],'fontsize',09);
Calib.Cores(5) = uicontrol(Calib.CoresG,'style','radiobutton','string','Ciano'   ,'units','normalized','position',[4/8 0 1/8 1],'backgroundcolor',[0.0 0.8 0.8],'fontsize',09);
Calib.Cores(6) = uicontrol(Calib.CoresG,'style','radiobutton','string','Azul'    ,'units','normalized','position',[5/8 0 1/8 1],'backgroundcolor',[0.0 0.0 0.8],'fontsize',09);
Calib.Cores(7) = uicontrol(Calib.CoresG,'style','radiobutton','string','Magenta' ,'units','normalized','position',[6/8 0 1/8 1],'backgroundcolor',[0.8 0.0 0.8],'fontsize',09);
Calib.Cores(8) = uicontrol(Calib.CoresG,'style','radiobutton','string','Total'   ,'units','normalized','position',[7/8 0 1/8 1],'backgroundcolor',[0.8 0.8 0.8],'fontsize',09,'value',1);

set(Calib.Cores,'visible','on')

% ==============================================
% Modelo de Cores: HSV
Calib.Painel(2) = uipanel(Calib.ID,...
    'Title','Modelo Cores - HSV',...
    'units','normalized',...
    'position',[0.0 0.75 1 0.15]);

% Cria o texto dos edits e dos sliders
Calib.HSV(1) = uicontrol(Calib.Painel(2),'style','text','string','Matiz'       ,'units','normalized','position',[0.02 0.6 0.3 0.25],'horizontalalignment','center','fontsize',10);
Calib.HSV(2) = uicontrol(Calib.Painel(2),'style','text','string','Saturação'   ,'units','normalized','position',[0.35 0.6 0.3 0.25],'horizontalalignment','center','fontsize',10);
Calib.HSV(3) = uicontrol(Calib.Painel(2),'style','text','string','Luminosidade','units','normalized','position',[0.67 0.6 0.3 0.25],'horizontalalignment','center','fontsize',10);

% Cria os edits para o padrão de cada cor
Calib.Edit(1) = uicontrol(Calib.Painel(2),'style','edit','string',0,  'units','normalized','position',[0.02 0.35 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');
Calib.Edit(2) = uicontrol(Calib.Painel(2),'style','edit','string',360,'units','normalized','position',[0.02 0.05 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');
Calib.Edit(3) = uicontrol(Calib.Painel(2),'style','edit','string',0,  'units','normalized','position',[0.35 0.35 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');
Calib.Edit(4) = uicontrol(Calib.Painel(2),'style','edit','string',100,'units','normalized','position',[0.35 0.05 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');
Calib.Edit(5) = uicontrol(Calib.Painel(2),'style','edit','string',0,  'units','normalized','position',[0.67 0.35 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');
Calib.Edit(6) = uicontrol(Calib.Painel(2),'style','edit','string',100,'units','normalized','position',[0.67 0.05 0.09 0.25],'horizontalalignment','center','callback','CalibEditAtualizar');

% Cria os sliders para o padrão de cada cor
Calib.Slider(1) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',360,'value',0,  'units','normalized','position',[0.12 0.35 0.2 0.25],'backgroundcolor',[0 0 0],'callback','CalibSliderAtualizar');
Calib.Slider(2) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',360,'value',360,'units','normalized','position',[0.12 0.05 0.2 0.25],'backgroundcolor',[1 1 1],'callback','CalibSliderAtualizar');
Calib.Slider(3) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',100,'value',0,  'units','normalized','position',[0.45 0.35 0.2 0.25],'backgroundcolor',[0 0 0],'callback','CalibSliderAtualizar');
Calib.Slider(4) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',100,'value',100,'units','normalized','position',[0.45 0.05 0.2 0.25],'backgroundcolor',[1 1 1],'callback','CalibSliderAtualizar');
Calib.Slider(5) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',100,'value',0,  'units','normalized','position',[0.77 0.35 0.2 0.25],'backgroundcolor',[0 0 0],'callback','CalibSliderAtualizar');
Calib.Slider(6) = uicontrol(Calib.Painel(2),'style','slider','Min',0,'Max',100,'value',100,'units','normalized','position',[0.77 0.05 0.2 0.25],'backgroundcolor',[1 1 1],'callback','CalibSliderAtualizar');

% ==============================================
% Botões
Calib.Painel(3) = uipanel(Calib.ID,...
    'Title','Botões',...
    'units','normalized',...
    'position',[0.0 0.65 1.0 0.10]);

% Cria os botões para segmentar as cores
Calib.Botoes(1) = uicontrol(Calib.Painel(3),'style','pushbutton','string','Selecionar Pixels'  ,'units','normalized','position',[0.01 0.1 0.2 0.8],'fontsize',09,'callback','CalibPixelsMontarTela');
Calib.Botoes(2) = uicontrol(Calib.Painel(3),'style','pushbutton','string','Salvar Calibração'  ,'units','normalized','position',[0.75 0.1 0.2 0.8],'fontsize',09,'callback','CalibSalvar' );

% ==============================================
% Campo Filtro
Calib.Painel(4) = uipanel(Calib.ID,...
    'Title','Opções de filtro',...
    'units','normalized',...
    'position',[0 0 0.4 0.65]);

Calib.Filtro(1) = uicontrol(Calib.Painel(4),'style','popup','string',{'Total','Matiz','Saturação','Iluminação','Filtro'},'units','normalized','position',[0.03 0.875 0.2 0.05],'fontsize',09,'callback','CalibProcessarImagem','enable','on');
Calib.Filtro(2) = uicontrol(Calib.Painel(4),'style','popup','string',{'','Filtro de Iluminação'},'units','normalized','position',[0.03 0.725 0.2 0.05],'fontsize',09,'enable','on', 'Value', 1, 'callback', 'FiltroBotaoOp; FiltroTelaAtualizar ; CalibProcessarImagem');
Calib.Filtro(3) = uicontrol(Calib.Painel(4),'style','pushbutton','string','Opções de Filtro'  ,'units','normalized','position',[0.03 0.575 0.2 0.075],'fontsize',09,'callback','FiltroTelaAbrir', 'enable','off');


% ==============================================
% Campo Segmentado
Calib.Painel(5) = uipanel(Calib.ID,...
    'Title','Campo segmentado',...
    'units','normalized',...
    'position',[0.4 0 0.6 0.65]);

Calib.Imagem.ID = subplot(1,1,1,'parent',Calib.Painel(5)); axis off
