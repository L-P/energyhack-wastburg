<?php

const BASE_URL = 'http://www.sofratherm.fr/index.php?pg=tableaux_mensuels';
const XPATH_TABLE = '//form/table//tr/td[2]';

exit(main());

function main()
{
    $start = strtotime('2000-01-01 00:00:00');
    $end = strtotime('first day of this month midnight');

    $data = scrap($start, $end);
    file_put_contents('raw', json_encode($data));
}

function scrap($start, $end)
{
    assert('$start && $end');

    $data = [];
    $cur = $start;
    for (
        $cur = $start;
        $cur <= $end;
        $cur = strtotime('first day of next month', $cur)
    ) {
        $month = (int) date('m', $cur);
        $year  = (int) date('Y', $cur);
        printf("Processing %u-%02u.\r", $year, $month);
        $data[$year][$month] = scrap_month($year, $month);
    }

    echo "Done.\n";
    return $data;
}


function scrap_month($year, $month)
{
    $raw = file_get_contents(BASE_URL, false, get_context($year, $month));
    $doc = new DOMDocument();
    @$doc->loadHTML($raw);
    $xpath = new DOMXpath($doc);
    $elements = $xpath->query(XPATH_TABLE);

    $data = [];
    foreach($elements as $e) {
        $data[] = $e->nodeValue;
    }

    array_pop($data); // ditch total
    $data = array_slice($data, 2); // ditch headers

    return array_map('floatval', $data);
}


function get_context($year, $month)
{
    return stream_context_create([
        'http' => [
            'method' => 'POST',
            'header'  => 'Content-type: application/x-www-form-urlencoded',
            'content' => http_build_query(compact('year', 'month')),
        ],
    ]);
}
