function newAngle = changeAngle(oldAngle)
% Essa função transforma um angulo entre [0 pi] U [0 -pi] para um angulo
% entre [0 2pi]

if 0 <= oldAngle <= pi
    newAngle = oldAngle;
else
    disp()
    newAngle = oldAngle + 2 * pi;
end


end