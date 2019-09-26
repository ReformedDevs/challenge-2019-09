<?php
    function generate_fibs($limit) {
        $nums = array();
        $prev = 1;
        $cur = 1;
        while ($cur < $limit) {
            if (substr(dechex(pow($cur, 2)), -1) == '9') {
                array_push($nums, $cur);
            }
            $temp = $cur;
            $cur = $prev + $cur;
            $prev = $temp;
        }

        return $nums;
    }

    function is_prime($number) {
        if ( $number == 1 ) {
            return false;
        }

        if ( $number == 2 ) {
            return true;
        }

        $x = sqrt($number);
        $x = floor($x);
        for ( $i = 2 ; $i <= $x ; ++$i ) {
            if ( $number % $i == 0 ) {
                break;
            }
        }
     
        if( $x == $i-1 ) {
            return true;
        } else {
            return false;
        }
    }

    function check_nums($nums) {
        foreach (array_reverse($nums) as $n) {
            if (is_prime($n)) {
                return $n;
            }
        }
    }

    function main($limit) {
        $start = (float) microtime() * 1000;
        $nums = generate_fibs($limit);
        $sol = check_nums($nums);
        $end = (float) microtime() * 1000;
        $format = 'specs, PHP, %s, %f, ¯\_(ツ)_/¯ ';
        printf($format, $sol, ($end - $start));
    }

    main(9000000000000000000);
?>