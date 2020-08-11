%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  agent.pl
%  Nine-Board Tic-Tac-Toe Agent
%  COMP3411/9414/9814 Artificial Intelligence
%  Alan Blair, CSE, UNSW

other(x,o).
other(o,x).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  mark(+P,+M,+SubBoard0,-SubBoard1)
%  mark move M for player P on SubBoard0 to produce SubBoard1
%
mark(P,1,[e|T],[P|T]).
mark(P,2,[A,e|T],[A,P|T]).
mark(P,3,[A,B,e|T],[A,B,P|T]).
mark(P,4,[A,B,C,e|T],[A,B,C,P|T]).
mark(P,5,[A,B,C,D,e|T],[A,B,C,D,P|T]).
mark(P,6,[A,B,C,D,E,e|T],[A,B,C,D,E,P|T]).
mark(P,7,[A,B,C,D,E,F,e|T],[A,B,C,D,E,F,P|T]).
mark(P,8,[A,B,C,D,E,F,G,e,I],[A,B,C,D,E,F,G,P,I]).
mark(P,9,[A,B,C,D,E,F,G,H,e],[A,B,C,D,E,F,G,H,P]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  play(+P,+L,+M,+Board0,-Board1)
%  mark move M for player P on board L of Board0 to produce Board1
%
play(_P,0,Board,Board).
play(P,1,M,[B|T],[B1|T]) :- mark(P,M,B,B1).
play(P,2,M,[C,B|T],[C,B1|T]) :- mark(P,M,B,B1).
play(P,3,M,[C,D,B|T],[C,D,B1|T]) :- mark(P,M,B,B1).
play(P,4,M,[C,D,E,B|T],[C,D,E,B1|T]) :- mark(P,M,B,B1).
play(P,5,M,[C,D,E,F,B|T],[C,D,E,F,B1|T]) :- mark(P,M,B,B1).
play(P,6,M,[C,D,E,F,G,B|T],[C,D,E,F,G,B1|T]) :- mark(P,M,B,B1).
play(P,7,M,[C,D,E,F,G,H,B|T],[C,D,E,F,G,H,B1|T]) :- mark(P,M,B,B1).
play(P,8,M,[C,D,E,F,G,H,I,B,K],[C,D,E,F,G,H,I,B1,K]) :- mark(P,M,B,B1).
play(P,9,M,[C,D,E,F,G,H,I,J,B],[C,D,E,F,G,H,I,J,B1]) :- mark(P,M,B,B1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  empty(-M,+SubBoard)
%  check that cell M of SubBoard is empty
%
empty(1,[e|_]).
empty(2,[_,e|_]).
empty(3,[_,_,e|_]).
empty(4,[_,_,_,e|_]).
empty(5,[_,_,_,_,e|_]).
empty(6,[_,_,_,_,_,e|_]).
empty(7,[_,_,_,_,_,_,e|_]).
empty(8,[_,_,_,_,_,_,_,e,_]).
empty(9,[_,_,_,_,_,_,_,_,e]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  legal(+L,-M,+Board)
%  true if cell M of board L is legal
%
legal(1,M,[B|_]) :- empty(M,B).
legal(2,M,[_,B|_]) :- empty(M,B).
legal(3,M,[_,_,B|_]) :- empty(M,B).
legal(4,M,[_,_,_,B|_]) :- empty(M,B).
legal(5,M,[_,_,_,_,B|_]) :- empty(M,B).
legal(6,M,[_,_,_,_,_,B|_]) :- empty(M,B).
legal(7,M,[_,_,_,_,_,_,B|_]) :- empty(M,B).
legal(8,M,[_,_,_,_,_,_,_,B,_]) :- empty(M,B).
legal(9,M,[_,_,_,_,_,_,_,_,B]) :- empty(M,B).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  subwin(+P,SubBoard)
%  true if player P has achieved 3-in-a-row
%
subwin(P,[P,P,P|_]).
subwin(P,[_,_,_,P,P,P|_]).
subwin(P,[_,_,_,_,_,_,P,P,P]).
subwin(P,[P,_,_,P,_,_,P,_,_]).
subwin(P,[_,P,_,_,P,_,_,P,_]).
subwin(P,[_,_,P,_,_,P,_,_,P]).
subwin(P,[P,_,_,_,P,_,_,_,P]).
subwin(P,[_,_,P,_,P,_,P,_,_]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  winning(+P,+L,+Board)
%  true if player P has achieved 3-in-a-row on board L
%
winning(P,1,[B|_]) :- subwin(P,B).
winning(P,2,[_,B|_]) :- subwin(P,B).
winning(P,3,[_,_,B|_]) :- subwin(P,B).
winning(P,4,[_,_,_,B|_]) :- subwin(P,B).
winning(P,5,[_,_,_,_,B|_]) :- subwin(P,B).
winning(P,6,[_,_,_,_,_,B|_]) :- subwin(P,B).
winning(P,7,[_,_,_,_,_,_,B|_]) :- subwin(P,B).
winning(P,8,[_,_,_,_,_,_,_,B,_]) :- subwin(P,B).
winning(P,9,[_,_,_,_,_,_,_,_,B]) :- subwin(P,B).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  open socket and establish TCP read/write streams
%
connect(Port) :-
   tcp_socket(Socket),
   gethostname(Host),
   tcp_connect(Socket,Host:Port),
   tcp_open_socket(Socket,INs,OUTs),
   assert(connectedReadStream(INs)),
   assert(connectedWriteStream(OUTs)).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  read next command and execute it
%
ttt :-
   connectedReadStream(IStream),
   read(IStream,Command),
   Command.

init :- ttt.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  start(+P)
%  start a new game for player P
%
start(P) :-
   retractall(board(_ )),
   retractall(player(_ )),
   retractall(prev_move(_ )),
   assert(board(
   [[e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e],[e,e,e,e,e,e,e,e,e]])),
   assert(player(P)),
   ttt.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  second_move(+K,+L)
%  assume first move is board K, cell L
%  choose second move and write it
%
second_move(K,L) :-
   retract(board(Board0)),
   player(P), other(P,Q),
   play(Q,K,L,Board0,Board1),
   print_board(Board1),
   search(P,L,Board1,M),
   play(P,L,M,Board1,Board2),
   print_board(Board2),
   assert(board(Board2)),
   assert(prev_move(M)),
   write_output(M),
   ttt.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  third_Move(+J,+K,+L)
%  assume first move is board K, cell L,
%           second move is board L, cell M
%  choose third move and write it
%
third_move(J,K,L) :-
   retract(board(Board0)),
   player(P),
   play(P,J,K,Board0,Board1),
   print_board(Board1),
   other(P,Q),
   play(Q,K,L,Board1,Board2),
   print_board(Board2),
   search(P,L,Board2,M),
   play(P,L,M,Board2,Board3),
   print_board(Board3),
   assert(board(Board3)),
   assert(prev_move(M)),
   write_output(M),
   ttt.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  next_move(+L)
%  assume opponent move is L
%  choose (our) next move and write it
%
next_move(L) :-
   retract(prev_move(K)),
   retract(board(Board0)),
   player(P), other(P,Q),
   play(Q,K,L,Board0,Board1),
   print_board(Board1),
   search(P,L,Board1,M),
   play(P,L,M,Board1,Board2),
   print_board(Board2),
   assert(board(Board2)),
   assert(prev_move(M)),
   write_output(M),
   ttt.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  search(+P,+L,+Board,-M)
%  choose Move M for player P on board L
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  search(+P,+Board,-M)
%  choose Move M for player P, by alpha-beta search
%
search(P,L,Board,Move) :-
   alpha_beta(P,L,5,Board,-2000,2000,Move,_Value).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  alpha_beta(+P,+D,+Board,+Alpha,+Beta,-Move,-Value)
%  perform alpha-beta search to depth D for player P,
%  assuming P is about to move on Board. Return Value
%  of current Board position, and best Move for P.

% if we have won, Value is 1000
alpha_beta(P,_L,_D,Board,_Alpha,_Beta,0,1000) :-
   winning(P,_,Board), ! .

% if other player has won, Value is -1000
alpha_beta(P,_L,_D,Board,_Alpha,_Beta,0,-1000) :-
   other(P,Q),
   winning(Q,_,Board), ! .

% if depth limit exceeded, use heuristic estimate
alpha_beta(P,L,0,Board,_Alpha,_Beta,0,Value) :-
   value(P,L,Board,Value), ! .

% evaluate and choose all legal moves in this position
alpha_beta(P,L,D,Board,Alpha,Beta,Move,Value) :-
   D > 0,
   findall(M,legal(L,M,Board),Moves),
   Moves \= [], !,
   Alpha1 is -Beta,
   Beta1 is -Alpha,
   D1 is D-1,
   eval_choose(P,L,Moves,Board,D1,Alpha1,Beta1,0,Move,Value).

% if no available moves, it must be a draw
alpha_beta(_P,_L,_D,_Board,_Alpha,_Beta,0,0).


% value predicate
value(P,L,[A,B,C,D,E,F,G,H,I],Value):-
   subboardvalue(P,A,ValueA),
   subboardvalue(P,B,ValueB),
   subboardvalue(P,C,ValueC),
   subboardvalue(P,D,ValueD),
   subboardvalue(P,E,ValueE),
   subboardvalue(P,F,ValueF),
   subboardvalue(P,G,ValueG),
   subboardvalue(P,H,ValueH),
   subboardvalue(P,I,ValueI),
   Values = [ValueA,ValueB,ValueC,ValueD,ValueE,ValueF,ValueG,ValueH,ValueI],
   valueHelper(Values,L,Value).
   %Value is ValueA +ValueB+ValueC +ValueD +ValueE +ValueF +ValueG +ValueH +ValueI.

valueHelper([], _, 0).
valueHelper([H|T],L,Value):-
   L =1,!,
   sumlist(T,ValueT),
   Value is H*2 + ValueT.
valueHelper([H|T], L, Value):-
   L1 is L-1,
   valueHelper(T, L1, ValueT),
   Value is H + ValueT.


subboardvalue(P,SubBoard,Value):-
   findall(ScoreP,subboardscore(P,SubBoard,ScoreP),ScoresP),
   sumlist(ScoresP,ValueP),
   other(P,Q),
   findall(ScoreQ,subboardscore(Q,SubBoard,ScoreQ),ScoresQ),
   sumlist(ScoresQ,ValueQ),
   Value is ValueP - ValueQ.

subboardscore(P,[P,P,e,_,_,_,_,_,_],50).
subboardscore(P,[P,e,P,_,_,_,_,_,_],50).
subboardscore(P,[e,P,P,_,_,_,_,_,_],50).
subboardscore(P,[_,_,_,P,P,e,_,_,_],50).
subboardscore(P,[_,_,_,P,e,P,_,_,_],50).
subboardscore(P,[_,_,_,e,P,P,_,_,_],50).
subboardscore(P,[_,_,_,_,_,_,P,P,e],50).
subboardscore(P,[_,_,_,_,_,_,P,e,P],50).
subboardscore(P,[_,_,_,_,_,_,e,P,P],50).

subboardscore(P,[P,_,_,P,_,_,e,_,_],50).
subboardscore(P,[P,_,_,e,_,_,P,_,_],50).
subboardscore(P,[e,_,_,P,_,_,P,_,_],50).
subboardscore(P,[_,P,_,_,P,_,_,e,_],50).
subboardscore(P,[_,P,_,_,e,_,_,P,_],50).
subboardscore(P,[_,e,_,_,P,_,_,P,_],50).
subboardscore(P,[_,_,P,_,_,P,_,_,e],50).
subboardscore(P,[_,_,P,_,_,e,_,_,P],50).
subboardscore(P,[_,_,e,_,_,P,_,_,P],50).

subboardscore(P,[P,_,_,_,P,_,_,_,e],50).
subboardscore(P,[P,_,_,_,e,_,_,_,P],50).
subboardscore(P,[e,_,_,_,P,_,_,_,P],50).
subboardscore(P,[_,_,P,_,P,_,e,_,_],50).
subboardscore(P,[_,_,P,_,e,_,P,_,_],50).
subboardscore(P,[_,_,e,_,P,_,P,_,_],50).


subboardscore(P,[P,e,e,_,_,_,_,_,_],10).
subboardscore(P,[e,e,P,_,_,_,_,_,_],10).
subboardscore(P,[e,P,e,_,_,_,_,_,_],10).
subboardscore(P,[_,_,_,P,e,e,_,_,_],10).
subboardscore(P,[_,_,_,e,e,P,_,_,_],10).
subboardscore(P,[_,_,_,e,P,e,_,_,_],10).
subboardscore(P,[_,_,_,_,_,_,P,e,e],10).
subboardscore(P,[_,_,_,_,_,_,e,e,P],10).
subboardscore(P,[_,_,_,_,_,_,e,P,e],10).

subboardscore(P,[P,_,_,e,_,_,e,_,_],10).
subboardscore(P,[e,_,_,e,_,_,P,_,_],10).
subboardscore(P,[e,_,_,P,_,_,e,_,_],10).
subboardscore(P,[_,P,_,_,e,_,_,e,_],10).
subboardscore(P,[_,e,_,_,e,_,_,P,_],10).
subboardscore(P,[_,e,_,_,P,_,_,e,_],10).
subboardscore(P,[_,_,P,_,_,e,_,_,e],10).
subboardscore(P,[_,_,e,_,_,e,_,_,P],10).
subboardscore(P,[_,_,e,_,_,P,_,_,e],10).

subboardscore(P,[P,_,_,_,e,_,_,_,e],10).
subboardscore(P,[e,_,_,_,e,_,_,_,P],10).
subboardscore(P,[e,_,_,_,P,_,_,_,e],10).
subboardscore(P,[_,_,P,_,e,_,e,_,_],10).
subboardscore(P,[_,_,e,_,e,_,P,_,_],10).
subboardscore(P,[_,_,e,_,P,_,e,_,_],10).



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  eval_choose(+P,+Moves,+Board,+D,+Alpha,+Beta,+BestMove
%              -ChosenMove,-Value)
%  Evaluate list of Moves and determine Value of position
%  as well as ChosenMove for this Board position
% (taking account of current BestMove for this position)

% if no more Moves, BestMove becomes ChosenMove and Value is Alpha
eval_choose(_P,_L,[],_Board,_D,Alpha,_Beta,BestMove,BestMove,Alpha).

% evaluate Moves, find Value of Board Position, and ChosenMove for P
eval_choose(P,L,[M|Moves],Board,D,Alpha,Beta,BestMove,ChosenMove,Value) :-
   play(P,L,M,Board,Board1),
   other(P,Q),
   alpha_beta(Q,M,D,Board1,Alpha,Beta,_Move1,Value1),
   V is -Value1,
   cutoff(P,L,Moves,Board,D,Alpha,Beta,BestMove,M,V,ChosenMove,Value).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  cutoff(+P,+Moves,+Board,+D,+Alpha,+Beta,+BestMove,+M,+V,
%              -ChosenMove,-Value)
%  Compare move M (with value V) to Alpha and Beta,
%  and compute Value and ChosenMove appropriately.

% cut off the search, ChosenMove is M and Value is V
cutoff(_P,_L,_Moves,_Board,_D,_Alpha,Beta,_Move0,M,V,M,V) :-
   V >= Beta.

% Alpha increases to V, BestMove is M, continue search
cutoff(P,L,Moves,Board,D,Alpha,Beta,_BestMove,M,V,ChosenMove,Value) :-
   Alpha < V, V < Beta,
   eval_choose(P,L,Moves,Board,D,V,Beta,M,ChosenMove,Value).

% keep searching, with same Alpha, Beta, BestMove
cutoff(P,L,Moves,Board,D,Alpha,Beta,BestMove,_M,V,ChosenMove,Value) :-
   V =< Alpha,
   eval_choose(P,L,Moves,Board,D,Alpha,Beta,BestMove,ChosenMove,Value).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  write_output(+M)
%  transmit the chosen move (M)
%
write_output(M) :-
   connectedWriteStream(OStream),
   write(OStream,M),
   nl(OStream), flush_output(OStream).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  print_board()
%
print_board([A,B,C,D,E,F,G,H,I]) :-
   print3boards(A,B,C),
   write('------+-------+------'),nl,
   print3boards(D,E,F),
   write('------+-------+------'),nl,
   print3boards(G,H,I),nl.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  print_board()
%
print3boards([A1,A2,A3,A4,A5,A6,A7,A8,A9],
             [B1,B2,B3,B4,B5,B6,B7,B8,B9],
             [C1,C2,C3,C4,C5,C6,C7,C8,C9]) :-
   print_line(A1,A2,A3,B1,B2,B3,C1,C2,C3),
   print_line(A4,A5,A6,B4,B5,B6,C4,C5,C6),
   print_line(A7,A8,A9,B7,B8,B9,C7,C8,C9).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  print_line()
%
print_line(A,B,C,D,E,F,G,H,I) :-
   write(A),write(' '),write(B),write(' '),write(C),write(' | '),
   write(D),write(' '),write(E),write(' '),write(F),write(' | '),
   write(G),write(' '),write(H),write(' '),write(I),nl.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%  last_move(+L)
%
last_move(L) :-
   retract(prev_move(K)),
   retract(board(Board0)),
   player(P), other(P,Q),
   play(Q,K,L,Board0,Board1),
   print_board(Board1),
   ttt.

win(_)  :- write('win'), nl,ttt.
loss(_) :- write('loss'),nl,ttt.
draw(_) :- write('draw'),nl,ttt.

end :- halt.
