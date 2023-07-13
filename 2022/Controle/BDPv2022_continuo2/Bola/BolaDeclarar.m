% Declaração da bola

Bola.X = zeros(1,2);
Bola.Xa = zeros(1,2);
Bola.dX = zeros(1,2);
Bola.Status = 0;

Bola2.X = zeros(1,2);
Bola2.ang = 0;
Bola3.X = zeros(1,2);

% Exibição da bola

    Bola.CAD   = [25*cos(linspace(-pi,pi,8));25*sin(linspace(-pi,pi,8));ones(1,8)];
    Bola.idCAD = patch(Bola.CAD(1,:),Bola.CAD(2,:),[1 0.5 0],'Parent',Partida.Ass.ID');

    Bola2.CAD   = [25*cos(linspace(-pi,pi,8));25*sin(linspace(-pi,pi,8));ones(1,8)];
    Bola2.idCAD = patch(Bola.CAD(1,:),Bola.CAD(2,:),[0 0 1],'Parent',Partida.Ass.ID');
    disp('entrou na bola azul')

    Bola3.CAD   = [25*cos(linspace(-pi,pi,8));25*sin(linspace(-pi,pi,8));ones(1,8)];
    Bola3.idCAD = patch(Bola.CAD(1,:),Bola.CAD(2,:),[0 1 1],'Parent',Partida.Ass.ID');
