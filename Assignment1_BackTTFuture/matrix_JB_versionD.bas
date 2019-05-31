'Compilers and Development of Libraries
'Assignment-1
'Simple code in BASIC
'Read 9 numbers from a file which represent a 3x3 matrix
'Multiply the read matrix by itself and print the result
'Alejandra Victoria
'Marcos Camarena
'May.2019

open "matrixV.txt" for input as #in
    line input #in, elem1$
    line input #in, elem2$
    line input #in, elem3$
    line input #in, elem4$
    line input #in, elem5$
    line input #in, elem6$
    line input #in, elem7$
    line input #in, elem8$
    line input #in, elem9$
    print elem1$
    print elem2$
    print elem3$
    print elem4$
    print elem5$
    print elem6$
    print elem7$
    print elem8$
    print elem9$
'close #in

'MatrixA$ = "3, 3,    1, 2, 3, 4, 5, 6, 7, 8, 9"
MatrixA$ = "3, 3,    elem1$, 2, 3, 4, 5, 6, 7, 8, 9"

MatrixA$(1,1) = "11"
MatrixA$(1,2) = "elem2$"
MatrixA$(1,3) = elem3$
MatrixA$(2,1) = elem4$
MatrixA$(2,2) = elem5$
MatrixA$(2,3) = elem6$
MatrixA$(3,1) = elem7$
MatrixA$(3,2) = elem8$
MatrixA$(3,3) = elem9$

close #in

print
print "3x3 Input Matrix"
call DisplayMatrix MatrixA$

print "Result of multiply Input Matrix by itself"
MatrixP$ =MatrixMultiply$( MatrixA$, MatrixA$)
call DisplayMatrix MatrixP$
print

wait

'______________________________________________________________________
'   Copy the functions below here onto the end of your LB program.

    function GetTerm( in$, i, j)    '   Return element( i along row, j down column)
        w =val( word$( in$, 1, ","))
        h =val( word$( in$, 2, ","))
        if (w <i) or ( h <j) then notice "Index lies outside matrix limits.": end
        GetTerm =val( word$( in$, 2 +i +( j -1) *w, ","))
    end function

    sub DisplayMatrix in$   '   Display looking like a matrix!
        w =val( word$( in$, 1, ","))
        h =val( word$( in$, 2, ","))
        'print "Width = "; w; " & height ="; h
        for i =0 to h -1
            print "         |";
            for j =1 to w
                term$ =word$( in$, j +2 +i *w, ",")
                print using( "#####", val( term$)),
                '   This formatting may not be a good general idea, but aids readability
            next j
            print "|"
        next i
        'print in$
        print
    end sub

    function MatrixMultiply$( inA$, inB$)
        AColumn =val( word$( inA$, 1, ","))          '  This holds number of COLUMNs
        ARow    =val( word$( inA$, 2, ","))          '                        ROWs
                                                     '  eg "1, 4,     1,2,3,4" is a column vector
        BColumn =val( word$( inB$, 1, ","))
        BRow    =val( word$( inB$, 2, ","))
        if ( AColumn <>BRow) or ( ARow <>BColumn) then notice "Matrix dimensions unsuitable. Not conformable": end
        n$ =str$( ARow); ","; str$( BRow); ","
        for AnsRow =1 to AColumn
            for AnsColumn =1 to BColumn
                trm =0
                for i =1 to BColumn
                    j1   =GetTerm( inB$, i, AnsRow)
                    j2   =GetTerm( inA$, AnsColumn, i)
                    trm  =trm + j1 *j2
                next i
                'if abs( trm) <1e-4 then trm =0  '   fiddled so acceptable in LB 4.03
                n$ =n$ +str$( trm) +","
            next AnsColumn
        next AnsRow
        MatrixMultiply$ =left$( n$, len( n$) -1) '   ############## trailing ',' to remove
    end function

