function mCADplotar(rBDP,LocalImagem)
if rBDP.pFlag.criado == 0
    rBDP.pFlag.criado = 1;
    % Exibição dos jogadores
    rBDP.pCAD.v    = [-35 -10 35 -10 -35; -35 -35 0 35 35; 1 1 1 1 1];
    rBDP.pCAD.id(1) = patch(rBDP.pCAD.v(1,:),rBDP.pCAD.v(2,:),rBDP.pCor,'Parent',LocalImagem);
    
    rBDP.pCAD.vd    = [-5 5 5 -5; -5 -5 5 5; 1 1 1 1];
    rBDP.pCAD.id(2) = patch(rBDP.pCAD.vd(1,:),rBDP.pCAD.vd(2,:),rBDP.pCor,'Parent',LocalImagem);
    rBDP.pCAD.id(2).FaceAlpha  = 0;
else
    rBDP.pCAD.id(1).Vertices   = ([cos(rBDP.pPos.X(3)) -sin(rBDP.pPos.X(3)) rBDP.pPos.X(1); sin(rBDP.pPos.X(3)) cos(rBDP.pPos.X(3)) rBDP.pPos.X(2); 0 0 1]*rBDP.pCAD.v)';
    rBDP.pCAD.id(1).FaceColor  = rBDP.pCor;
    rBDP.pCAD.id(1).EdgeColor  = rBDP.pTime;
    
    rBDP.pCAD.id(2).Vertices   = ([1 0 rBDP.pPos.Xd(1); 0 1 rBDP.pPos.Xd(2); 0 0 1]*rBDP.pCAD.vd)';    
    rBDP.pCAD.id(2).EdgeColor  = rBDP.pCor;   
end

end