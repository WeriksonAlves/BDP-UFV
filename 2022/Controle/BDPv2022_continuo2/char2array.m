function array = char2array(charLoss)

array = [];
arrayAux = "";
sizeArray = length(charLoss);
for i=1:sizeArray
    if charLoss(i) ~= " " && i ~= sizeArray
        arrayAux = arrayAux + charLoss(i);
    else
        array = [array; str2num(arrayAux)];
        arrayAux = "";
    end

end