% Distância mínima coletiva
% Testar a distância entre os jogadores e as camisas
% Posicionar os jogadores e  associar às camisas mais próximas
% coletivamente

clear all
%close all
clc

figure
axis([-10 10 -10 10])
hold

nc = input('Num Jogadores: ');
nn = input('Num Camisas: ');

Xc = ginput(nc);
plot(Xc(:,1),Xc(:,2),'*b'),
Xn = ginput(nn);
plot(Xn(:,1),Xn(:,2),'sr')

tic
for  ii = 1:size(Xc,1)
    for  jj = 1:size(Xn,1)
        D(ii,jj) = norm(Xc(ii,:)-Xn(jj,:));
    end
end

numCam = size(Xc,1);
numNum = size(Xn,1);

% Número de Jogadores menor que o número de camisas
if numCam <= numNum
    switch size(Xc,1)
        case 1
            dmin = [1 0 0 10000];
            % Caso completo de jogadores e camisas
            for  ii = 1:size(Xn,1)
                if dmin(4) > D(1,ii)
                    dmin = [ii 0 0 D(1,ii)];
                end
            end
            
        case 2
            dmin = [1 2 0 10000];
            % Caso completo de jogadores e camisas
            for  ii = 1:size(Xn,1)
                for  jj = 1:size(Xn,1)
                    if ii ~= jj
                        if dmin(4) > D(1,ii)+D(2,jj)
                            dmin = [ii jj 0 D(1,ii)+D(2,jj)];
                        end
                    end
                end
            end
            
        case 3
            dmin = [1 2 3 10000];
            % Caso completo de jogadores e camisas
            for  ii = 1:size(Xn,1)
                for  jj = 1:size(Xn,1)
                    for  kk = 1:size(Xn,1)
                        if ii ~= jj && ii ~= kk && jj ~= kk
                            if dmin(4) > D(1,ii)+D(2,jj)+D(3,kk)
                                dmin = [ii jj kk D(1,ii)+D(2,jj)+D(3,kk)];
                            end
                        end
                    end
                end
            end
    end
else
    % Situação de identificar mais jogadores que camisas
    
    switch size(Xn,1)
        case 1 % Uma camisa
            dmin = [0 0 0 10000];
            for  ii = 1:size(Xc,1)
                if dmin(4) > D(ii,1)
                    dmin = [0 0 0 10000];
                    dmin(ii) = 1;
                    dmin(4) = D(ii,1);
                end
            end
            
        case 2 % Duas camisas
            dmin = [0 0 0 10000];
            p =   [3     2     1
                3     1     2
                2     3     1
                2     1     3
                1     3     2
                1     2     3];
            for ii = 1:size(p,1)
                if dmin(4) > D(p(ii,1),1)+D(p(ii,2),2)
                    dmin(p(ii,1)) = 1;
                    dmin(p(ii,2)) = 2;
                    dmin(p(ii,3)) = 0;
                    dmin(4) = D(p(ii,1),1)+D(p(ii,2),2);
                end
            end
            
    end
end
toc

for mm = 1:size(Xc,1)
    if dmin(mm) > 0
        h(mm)   = plot([Xc(mm,1) Xn(dmin(mm),1)],[Xc(mm,2) Xn(dmin(mm),2)]);
        tx(mm)  = text(Xc(mm,1),Xc(mm,2),['Xc_{' num2str(mm) '}']);
        txd(mm) = text(Xn(dmin(mm),1),Xn(dmin(mm),2),['Xn_{' num2str(dmin(mm)) '}']);
    end
end


