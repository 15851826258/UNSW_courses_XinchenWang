%COMP9414 Assignment1 XINCHEN WANG z5197409

%Q1
%fuc to check even or odd
iseven(H):-
    0 =:= H mod 2.

%base case
sumsq_even([],0).

%recursive case
sumsq_even([H|T],Sum):-
    sumsq_even(T,Sum_new),
    iseven(H),%is even
    This is H * H,
    Sum is This + Sum_new.%add to the result

sumsq_even([H|T],Sum):-
    sumsq_even(T,Sum_new),
    not(iseven(H)),%is odd
    Sum is Sum_new.%odd so don't calcuate

%Q2
father(Father,Child):-
    male(Father),
    parent(Father,Child).

maleancestor(Per1,Per2):-%exit of recursion
    Per1=Per2.%the same people

maleancestor(Per1,Per2):-
    father(Per3,Per2),
    maleancestor(Per1,Per3).

same_name(Per1,Per2):-
    maleancestor(X,Per1),
    maleancestor(X,Per2).

%Q3
%base case
sqrt_list([],[]).

%recursive case
sqrt_list([H|T],[[H,Sqrt_num]|Result]):-
    Sqrt_num is sqrt(H),
    sqrt_list(T,Result).

%Q4
%fucs for same range check
same(Num1,Num2):-
    Num1 >= 0 , Num2 >= 0.
same(Num1,Num2):-
    Num1 < 0 , Num2 < 0.

%base case
sign_runs([],[]).

%recursive case
sign_runs([Head|Tail],Result):-
    sign_runs(Tail,Rest),
    result_ap(Head,Rest,Result).%fucs to add ele

%add ele to the result
result_ap(Head,Rest,Result):-
    Rest == [] ,
    Result=[[Head]].

%the num are the same
result_ap(Head,Rest,Result):-
    Rest=[[H|T]|R],
    same(H,Head),%situation that is the same signal
    This=[Head|[H|T]],%combine the same signal into one ele
    Result=[This|R].%combine to the result

%the mun are not the same
result_ap(Head,Rest,Result):-
    Rest=[[H|_A]|_B],
    \+same(H,Head),%situation that is not same signal
    This=[Head],%create a new ele
    Result=[This|Rest].%add to the result


% Q5
% base case the child branch
is_heap(tree(empty,_,empty)).

%right child is empty
is_heap(tree(Left,Value,empty)):-
    Left = tree(_,Left_Value,_),
    Value =< Left_Value ,
    is_heap(Left).%recursion for left

%left child is empty
is_heap(tree(empty,Value,Right)):-
    Right = tree(_,Right_Value,_),
    Value =< Right_Value,%check the
    is_heap(Right).%recursion for right

%No children is empty
is_heap(tree(Left,Value,Right)):-
    Left=tree(_,Left_Value,_),
    Right=tree(_,Right_Value,_),
    Value=<Left_Value,
    Value=<Right_Value,
    is_heap(Left),%recursion for left
    is_heap(Right).%recursion for right
