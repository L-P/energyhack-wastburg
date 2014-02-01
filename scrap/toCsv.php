<?php

exit(main());

function main()
{
    $raw = json_decode(file_get_contents('raw.json'), true);
    $csv = fopen('dju.csv', 'w+');
    foreach($raw as $year => $perMonth) {
        foreach($perMonth as $month => $list) {
            foreach($list as $day => $value) {
                fputcsv($csv, [
                    sprintf('%u-%02u-%02u', $year, $month, $day + 1),
                    $value
                ]);
            }
        }
    }
    fclose($csv);
}
