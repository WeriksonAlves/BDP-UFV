Filtro.TitleID(1) = uicontrol(Filtro.ID,'style','text','string','','units','normalized','position',[0.05 0.825 0.9 0.15],'horizontalalignment','center','fontsize',12);
Filtro.TitleID(2) = uicontrol(Filtro.ID,'style','text','string','','units','normalized','position',[0.05 -0.1 0.9 0.15],'horizontalalignment','left','fontsize',9);
Filtro.TitleID(1).String = Calib.Filtro.Usado.String{Calib.Filtro.Usado.Value};

switch Calib.Filtro.Usado.Value
    case 2
        Filtro.Control.Title(1) = uicontrol(Filtro.ID,'style','text','string','Tipo de Filtro:','units','normalized','position',[0.05 0.85 0.9 0.05],'horizontalalignment','center','fontsize',10);
        Filtro.Control.Tipo(1) = uicontrol(Filtro.ID,'style','popup','string',{'square','disk','line','diamond','octagon'},'units','normalized','position',[0.2 0.8 0.6 0.05],'horizontalalignment','center','fontsize',10,'Callback', 'FiltroDadosAtualizarIlu');
        
        Filtro.Control.Texto(1) = uicontrol(Filtro.ID,'style','text','string','Largura do quadrado'       ,'units','normalized','position',[0.05 0.7 0.9 0.05],'horizontalalignment','center','fontsize',10);
        Filtro.Control.Valor(1) = uicontrol(Filtro.ID,'style','edit','string',15,  'units','normalized','position',[0.2 0.65 0.6 0.05],'horizontalalignment','center', 'callback','FiltroDadosAtualizarIlu;CalibProcessarImagem;FiltroAtualizarTempo');
        Filtro.Control.Texto(2) = uicontrol(Filtro.ID,'style','text','string',''       ,'units','normalized','position',[0.05 0.55 0.9 0.05],'horizontalalignment','center','fontsize',10, 'Visible','off');
        Filtro.Control.Valor(2) = uicontrol(Filtro.ID,'style','edit','string',15,  'units','normalized','position',[0.2 0.5 0.6 0.05],'horizontalalignment','center', 'Visible','off', 'callback','FiltroDadosAtualizarIlu;CalibProcessarImagem;FiltroAtualizarTempo');
        
        FiltroDadosAtualizarIlu
end
