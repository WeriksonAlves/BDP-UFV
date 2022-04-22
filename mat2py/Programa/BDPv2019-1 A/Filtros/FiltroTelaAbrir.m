switch get(Calib.Filtro.Usado,'enable')
    case 'on'
        set(Filtro.ID,'Visible','on')
        set(Calib.Filtro.Usado,'enable','off')
    case 'off'
        FiltroTelaFechar
end