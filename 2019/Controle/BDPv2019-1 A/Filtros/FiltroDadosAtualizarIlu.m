
switch Filtro.Control.Tipo(1).Value
    case 1    
        set(Filtro.Control.Texto(1), 'String','Largura do quadrado');
        set(Filtro.Control.Texto(2), 'Visible','off');
        set(Filtro.Control.Valor(2), 'Visible','off');
        Filtro.Comando = strcat('strel(','''square'',',Filtro.Control.Valor(1).String,')');
    case 2
        set(Filtro.Control.Texto(1), 'String','Raio do circulo');
        set(Filtro.Control.Texto(2), 'Visible','off');
        set(Filtro.Control.Valor(2), 'Visible','off');
        Filtro.Comando = strcat('strel(','''disk'',',Filtro.Control.Valor(1).String,')');
    case 3
        set(Filtro.Control.Texto(1), 'String','Largura da linha');
        set(Filtro.Control.Texto(2), 'Visible','on','String','Ângulo da linha');
        set(Filtro.Control.Valor(2), 'Visible','on');
        Filtro.Comando = strcat('strel(','''line'',',Filtro.Control.Valor(1).String,',',Filtro.Control.Valor(2).String,')');
    case 4        
        set(Filtro.Control.Texto(1), 'String','Tamanho do losango');
        set(Filtro.Control.Texto(2), 'Visible','off');
        set(Filtro.Control.Valor(2), 'Visible','off');
        Filtro.Comando = strcat('strel(','''diamond'',',Filtro.Control.Valor(1).String,')');
    case 5
        set(Filtro.Control.Texto(1), 'String','Tamanho do octógono (x3)');
        set(Filtro.Control.Texto(2), 'Visible','off');
        set(Filtro.Control.Valor(2), 'Visible','off');
        Filtro.Comando = strcat('strel(','''octagon'',',Filtro.Control.Valor(1).String,')');
end
