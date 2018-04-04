function note=GenerateNoteStructure()
v=1;
count=0;
for z=1:108
    if v>12
        v=v-12;
        count=count+1;
    end
    
    if v==1
        note(z).name=sprintf('C%d',count);
    elseif v==2
        note(z).name=sprintf('C#/Db(%d)',count);
    elseif v==3
        note(z).name=sprintf('D%d',count);
    elseif v==4
        note(z).name=sprintf('D#/Eb(%d)',count); 
    elseif v==5
        note(z).name=sprintf('E%d',count);
    elseif v==6
        note(z).name=sprintf('F%d',count);
    elseif v==7
        note(z).name=sprintf('F#/Gb(%d)',count);
    elseif v==8
        note(z).name=sprintf('G%d',count);
    elseif v==9
        note(z).name=sprintf('G#/Ab(%d)',count);
    elseif v==10
        note(z).name=sprintf('A%d',count);
    elseif v==11
        note(z).name=sprintf('A#/Bb(%d)',count);
    elseif v==12
        note(z).name=sprintf('B%d',count);
    end
    v=v+1;
note(z).freq=16.3516*power(2,(z-1)/12);
end
end


%-----some shit that didnt work-------------
% if v>12
%     v=v-12;
%     count=count+1;
% end
% if v<=6
%  if mod(v,2)==1
%      note(z).name=sprintf(strcat(char(66+v),'%d'),count);
%  else
%      if v==6
%          note(z).name=sprintf('F%d',count);
%      else
%          note(z).name=sprintf(strcat(char(66+(v-1)),'#/',char(66+v),'b(%d)'),count);
%      end
%  end
% else
%     if mod(v,2)==0
%      note(z).name=sprintf(strcat(char(66+v),'%d'),count);
%     else
%          note(z).name=sprintf(strcat(char(66+(v-1)),'#/',char(66+v),'b(%d)'),count);
%     end
% end
% v=v+1;
     
