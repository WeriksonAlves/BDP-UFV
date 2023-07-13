%% Inicia a tela de calibração de cores

% Inicia e modifica os parâmetros da tela de calibração e chama a função FecharCalibracao para fechar

% ==============================================
% Calibração do Campo
Campo.Painel(1) = uipanel(Campo.ID,...
    'Title','Calibrar Campo',...
    'units','normalized',...
    'position',[0 0.8 1 0.2]);

% Cria os botões para segmentar as cores
Campo.Botoes(1) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Capturar Imagem'     ,'units','normalized','position',[0.05 0.55 0.24 0.3],'fontsize',09,'callback','CampoCapturarImagem'      ,'enable','on');
Campo.Botoes(2) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Recortar Imagem'     ,'units','normalized','position',[0.38 0.55 0.24 0.3],'fontsize',09,'callback','CampoRecortarFazer'       ,'enable','on');
Campo.Botoes(3) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Anular Recorte'      ,'units','normalized','position',[0.70 0.55 0.24 0.3],'fontsize',09,'callback','CampoRecortarAnular'      ,'enable','on');
Campo.Botoes(4) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Correlacionar pontos','units','normalized','position',[0.05 0.05 0.24 0.3],'fontsize',09,'callback','CampoCorrelacionarPontos' ,'enable','on');
Campo.Botoes(5) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Validar pontos'      ,'units','normalized','position',[0.38 0.05 0.24 0.3],'fontsize',09,'callback','CampoValidarPontos'       ,'enable','on');
Campo.Botoes(6) = uicontrol(Campo.Painel(1),'style','pushbutton','string','Salvar Calibração'   ,'units','normalized','position',[0.70 0.05 0.24 0.3],'fontsize',09,'callback','CampoSalvar'              ,'enable','on');

% ==============================================
% Campo Padrão
Campo.Painel(2) = uipanel(Campo.ID,...
    'Title','Campo Padrão',...
    'units','normalized',...
    'position',[0 0 0.4 0.8]);

Campo.Padrao.ID = subplot(1,1,1,'parent',Campo.Painel(2));

% Desenho do Campo de Jogo
Campo.Padrao.Coord = [...
    -750 -650  750 -650;
    750 -650  750  650;
    750  650 -750  650;
    -750  650 -750 -650;
    000 -650  000  650;
    -750 -350 -600 -350;
    -600 -350 -600  350;
    -600  350 -750  350;
    750 -350  600 -350;
    600 -350  600  350;
    600  350  750  350];

Campo.Padrao.idPontos = [...
    -750 -650;
    000 -650;
    750 -650;
    750  650;
    000  650;
    -750  650;
    -600  350;
    -600 -350;
    600 -350;
    600  350];

Campo.Padrao.XY(:,:,1) = [-950  950  950 -950; -800 -800 800 800];
Campo.Padrao.XY(:,:,2) = [-750  000  000 -750; -650 -650 650 650];
Campo.Padrao.XY(:,:,3) = [ 000  750  750  000; -650 -650 650 650];
Campo.Padrao.XY(:,:,4) = [-750 -600 -600 -750; -350 -350 350 350];
Campo.Padrao.XY(:,:,5) = [ 600  750  750  600; -350 -350 350 350];

Campo.Padrao.fig(1) = patch(Campo.Padrao.XY(1,:,1),Campo.Padrao.XY(2,:,1),[0 0 0],'Parent',Campo.Padrao.ID,'EdgeColor',[0 0 0]);
for ii = 2:5
    Campo.Padrao.fig(ii) = patch(Campo.Padrao.XY(1,:,ii),Campo.Padrao.XY(2,:,ii),[0 0 0], 'Parent',Campo.Padrao.ID,'EdgeColor',[1 1 1]);
end

axis equal
axis off


% ==============================================
% Campo Real
Campo.Painel(3) = uipanel(Campo.ID,...
    'Title','Campo Real',...
    'units','normalized',...
    'position',[0.4 0 0.6 0.8]);

Campo.Real.ID = subplot(1,1,1,'parent',Campo.Painel(3)); axis off
