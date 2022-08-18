%% Inicia a tela de calibração de cores

% ==============================================
% Flags de controle da partida
Partida.emJogo = 0;
Partida.ta     = 0.1; % [s] tempo de amostragem

% ==============================================
% Inicia e modifica os parâmetros da tela de calibração e chama a função FecharCalibracao para fechar

% ==============================================
% Definição dos jogadaores
Partida.Painel(1) = uipanel(Partida.ID,...
    'Title','Definição do time',...
    'units','normalized',...
    'position',[0 0.6 0.2 0.4]);

% Selecionar a cor do time
Partida.CorTimeG(1) = uibuttongroup(Partida.Painel(1),'units','normalized','position',[0 0.8 1 0.2],'selectionchangedfcn','PartidaSelecionar');
Partida.CorTime(1) = uicontrol(Partida.CorTimeG(1),'style','radiobutton','string','Amarelo','units','normalized','position',[0   0 1/2 1],'backgroundcolor',[1 1 0],'fontsize',09);
Partida.CorTime(2) = uicontrol(Partida.CorTimeG(1),'style','radiobutton','string','Ciano'  ,'units','normalized','position',[1/2 0 1/2 1],'backgroundcolor',[0 1 1],'fontsize',09);

% Selecionar o lado de ataque
Partida.LadoG(1) = uibuttongroup(Partida.Painel(1),'units','normalized','position',[0 0.6 1 0.2],'selectionchangedfcn','PartidaSelecionar');
Partida.Lado(1) = uicontrol(Partida.LadoG(1),'style','radiobutton','string','<<< - - -','units','normalized','position',[0   0 1/2 1],'backgroundcolor',[0.7 0.7 0.7],'fontsize',09);
Partida.Lado(2) = uicontrol(Partida.LadoG(1),'style','radiobutton','string','+ + + >>>','units','normalized','position',[1/2 0 1/2 1],'backgroundcolor',[0.9 0.9 0.9],'fontsize',09);

% Jogadores em campo
% Informação dos jogadores
Partida.Camisa(1) = uicontrol(Partida.Painel(1),'style','popup','string',{'Vermelho','Verde','Azul','Magenta',''},'units','normalized','position',[0 0.4 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',1);
Partida.Camisa(2) = uicontrol(Partida.Painel(1),'style','popup','string',{'Vermelho','Verde','Azul','Magenta',''},'units','normalized','position',[0 0.2 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',2);
Partida.Camisa(3) = uicontrol(Partida.Painel(1),'style','popup','string',{'Vermelho','Verde','Azul','Magenta',''},'units','normalized','position',[0 0.0 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',4);
 
% Função do jogador
Partida.Funcao(1) = uicontrol(Partida.Painel(1),'style','popup','string',{'Goleiro','Defesa','Ataque'},'units','normalized','position',[0.5 0.4 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',1);
Partida.Funcao(2) = uicontrol(Partida.Painel(1),'style','popup','string',{'Goleiro','Defesa','Ataque'},'units','normalized','position',[0.5 0.2 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',2);
Partida.Funcao(3) = uicontrol(Partida.Painel(1),'style','popup','string',{'Goleiro','Defesa','Ataque'},'units','normalized','position',[0.5 0.0 0.5 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',3);

% CoresPrinUsadas(1) = uicontrol(Partida.Painel(1),'style','popup','string',{'Escanear cores principais','Time BDP e bola','Time BDP'},'units','normalized','position',[0 0.15 1/3 0.2],'fontsize',09,'callback','PartidaSelecionar','enable','on','Value',1);

% ==============================================
% Parâmetros dos jogadores
Partida.Painel(2) = uipanel(Partida.ID,...
    'Title','Parâmetros dos jogadores',...
    'units','normalized',...
    'position',[0.21 0.6 0.59 0.4]);

Partida.Tabela = uitable(Partida.Painel(2),...
        'RowName',{'X [mm]','Xd [mm]','Psi [°]','U [x/s]', 'W [rad/s]', 'PWM [byte]','Ganho AN','Ganho BN'},...
        'ColumnName',{'BDP1','','BPD2','','BDP3',''},...
        'Data',zeros(7,6),...
        'ColumnEditable',true,...
        'CellEditCallback','PartidaDadosAtualizar',...
        'units','normalized',...
        'position',[0.01 0.01 0.98 0.98]);

% ==============================================
Partida.Painel(6) = uipanel(Partida.ID,...
    'Title','Botões de interação',...
    'units','normalized',...
    'position',[0.81 0.6 0.18 0.4]);

Partida.Botoes(1) = uicontrol(Partida.Painel(6),'style','pushbutton','string','Começar Partida' ,'units','normalized','position',[0.0 0.8 1 0.2],'fontsize',09,'callback','PartidaIniciar'   ,'enable','on');
Partida.Botoes(2) = uicontrol(Partida.Painel(6),'style','pushbutton','string','Parar Partida'   ,'units','normalized','position',[0.0 0.6 1 0.2],'fontsize',09,'callback','PartidaParar'     ,'enable','on');
Partida.Botoes(4) = uicontrol(Partida.Painel(6),'style','pushbutton','string','Iniciar Jogo'    ,'units','normalized','position',[0.0 0.2 1 0.2],'fontsize',09,'callback','PartidaRecomecar' ,'enable','on');
Partida.Botoes(5) = uicontrol(Partida.Painel(6),'style','pushbutton','string','Pausar Jogo'     ,'units','normalized','position',[0.0 0.0 1 0.2],'fontsize',09,'callback','PartidaPausar'    ,'enable','on');


% ==============================================
% Vistas
Partida.Painel(3) = uipanel(Partida.ID,...
    'Title','Visão Câmera :: Segmentação :: Associação',...
    'units','normalized',...
    'BackgroundColor',[0 0 0],...
    'ForegroundColor',[1 1 1],...
    'position',[0 0 1 0.6]);

Partida.Cam.ID = subplot(1,3,1,'parent',Partida.Painel(3)); axis off
set(Partida.Cam.ID,'Position',[0/3 0 1/3 0.9]);
Partida.Seg.ID = subplot(1,3,2,'parent',Partida.Painel(3)); axis off
set(Partida.Seg.ID,'Position',[1/3 0 1/3 0.9]);
Partida.Ass.ID = subplot(1,3,3,'parent',Partida.Painel(3)); axis off
set(Partida.Ass.ID,'Position',[2/3 0 1/3 0.9]);

% Desenho do Campo de Jogo
Partida.Ass.fig(1) = patch(Campo.Padrao.XY(1,:,1),Campo.Padrao.XY(2,:,1),[0 0 0],'Parent',Partida.Ass.ID,'EdgeColor',[0 0 0]);
for ii = 2:5
    Partida.Ass.fig(ii) = patch(Campo.Padrao.XY(1,:,ii),Campo.Padrao.XY(2,:,ii),[0 0 0],'Parent',Partida.Ass.ID,'EdgeColor',[1 1 1],'FaceAlpha',0);
end
axis equal
axis off

% ==============================================
% Vizualização do jogo
Partida.Visual(1) = uicontrol(Partida.Painel(3),'style','checkbox','string','Visão Câmera     ','units','normalized','position',[0/3 0.9 1/3 0.1],'fontsize',09,'enable','on','BackgroundColor',[0 0 0],'ForegroundColor',[1 1 1],'Value',0);
Partida.Visual(2) = uicontrol(Partida.Painel(3),'style','checkbox','string','Visão Segmentação','units','normalized','position',[1/3 0.9 1/3 0.1],'fontsize',09,'enable','on','BackgroundColor',[0 0 0],'ForegroundColor',[1 1 1],'Value',0);
Partida.Visual(3) = uicontrol(Partida.Painel(3),'style','checkbox','string','Visão Associação ','units','normalized','position',[2/3 0.9 1/3 0.1],'fontsize',09,'enable','on','BackgroundColor',[0 0 0],'ForegroundColor',[1 1 1],'Value',1);

% ==============================================
% Criar jogadores e bola
for ii = 1:3
    % Jogadores BDP
    JogBDP(ii) = Patola;
    JogBDP(ii).mCADplotar(Partida.Ass.ID);
    
    % Jogadores Adversários
    JogAdv(ii) = Adversario;
    JogAdv(ii).mCADplotar(Partida.Ass.ID);
end
BolaDeclarar