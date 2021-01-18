# Generated by Django 3.1.4 on 2021-01-16 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210115_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('TPE', 'TPE'), ('KZT', 'KZT'), ('CHE', 'CHE'), ('CLF', 'CLF'), ('QAR', 'QAR'), ('PHP', 'PHP'), ('MRO', 'MRO'), ('SZL', 'SZL'), ('MZM', 'MZM'), ('YUR', 'YUR'), ('KYD', 'KYD'), ('BDT', 'BDT'), ('XDR', 'XDR'), ('SSP', 'SSP'), ('ZWD', 'ZWD'), ('KHR', 'KHR'), ('TTD', 'TTD'), ('HNL', 'HNL'), ('BIF', 'BIF'), ('MLF', 'MLF'), ('ARL', 'ARL'), ('XFO', 'XFO'), ('IRR', 'IRR'), ('EUR', 'EUR'), ('FRF', 'FRF'), ('VES', 'VES'), ('CSK', 'CSK'), ('MKN', 'MKN'), ('XFU', 'XFU'), ('CNH', 'CNH'), ('NOK', 'NOK'), ('MWK', 'MWK'), ('BEC', 'BEC'), ('ARP', 'ARP'), ('SUR', 'SUR'), ('ZWL', 'ZWL'), ('GTQ', 'GTQ'), ('BRC', 'BRC'), ('XPF', 'XPF'), ('AFN', 'AFN'), ('GRD', 'GRD'), ('MAF', 'MAF'), ('ARS', 'ARS'), ('TRY', 'TRY'), ('BEL', 'BEL'), ('NPR', 'NPR'), ('ANG', 'ANG'), ('NIO', 'NIO'), ('THB', 'THB'), ('BRE', 'BRE'), ('ZMW', 'ZMW'), ('GIP', 'GIP'), ('ALK', 'ALK'), ('INR', 'INR'), ('AZN', 'AZN'), ('MRU', 'MRU'), ('UGX', 'UGX'), ('HRK', 'HRK'), ('UAK', 'UAK'), ('ARM', 'ARM'), ('ZMK', 'ZMK'), ('LVR', 'LVR'), ('ESA', 'ESA'), ('PEI', 'PEI'), ('AOK', 'AOK'), ('BRN', 'BRN'), ('ZRZ', 'ZRZ'), ('ESB', 'ESB'), ('LVL', 'LVL'), ('PEN', 'PEN'), ('XBC', 'XBC'), ('MGF', 'MGF'), ('IQD', 'IQD'), ('BGL', 'BGL'), ('PYG', 'PYG'), ('LAK', 'LAK'), ('UYU', 'UYU'), ('VNN', 'VNN'), ('VEF', 'VEF'), ('GWP', 'GWP'), ('LUL', 'LUL'), ('KGS', 'KGS'), ('ILP', 'ILP'), ('MCF', 'MCF'), ('BAN', 'BAN'), ('ESP', 'ESP'), ('OMR', 'OMR'), ('XRE', 'XRE'), ('CZK', 'CZK'), ('GEL', 'GEL'), ('GHS', 'GHS'), ('ISK', 'ISK'), ('RSD', 'RSD'), ('UYI', 'UYI'), ('KMF', 'KMF'), ('MXV', 'MXV'), ('MTL', 'MTL'), ('USS', 'USS'), ('AZM', 'AZM'), ('VUV', 'VUV'), ('MMK', 'MMK'), ('SAR', 'SAR'), ('CSD', 'CSD'), ('ZAL', 'ZAL'), ('KRH', 'KRH'), ('BAM', 'BAM'), ('GMD', 'GMD'), ('ATS', 'ATS'), ('ETB', 'ETB'), ('EGP', 'EGP'), ('YUD', 'YUD'), ('HTG', 'HTG'), ('RON', 'RON'), ('ITL', 'ITL'), ('BTN', 'BTN'), ('SDG', 'SDG'), ('BRR', 'BRR'), ('YER', 'YER'), ('NAD', 'NAD'), ('AED', 'AED'), ('EEK', 'EEK'), ('MDL', 'MDL'), ('SOS', 'SOS'), ('CNY', 'CNY'), ('BRL', 'BRL'), ('MGA', 'MGA'), ('CHF', 'CHF'), ('MVP', 'MVP'), ('MTP', 'MTP'), ('CUP', 'CUP'), ('PLN', 'PLN'), ('TOP', 'TOP'), ('ARA', 'ARA'), ('CRC', 'CRC'), ('LYD', 'LYD'), ('TJS', 'TJS'), ('COP', 'COP'), ('ECV', 'ECV'), ('VEB', 'VEB'), ('LUC', 'LUC'), ('GBP', 'GBP'), ('BUK', 'BUK'), ('GNF', 'GNF'), ('SDP', 'SDP'), ('STD', 'STD'), ('GWE', 'GWE'), ('BOL', 'BOL'), ('LTT', 'LTT'), ('FIM', 'FIM'), ('MXN', 'MXN'), ('SGD', 'SGD'), ('XUA', 'XUA'), ('SYP', 'SYP'), ('HRD', 'HRD'), ('ZRN', 'ZRN'), ('BAD', 'BAD'), ('BYR', 'BYR'), ('BOB', 'BOB'), ('VND', 'VND'), ('TMT', 'TMT'), ('LKR', 'LKR'), ('NGN', 'NGN'), ('MYR', 'MYR'), ('AON', 'AON'), ('DDM', 'DDM'), ('FJD', 'FJD'), ('CLP', 'CLP'), ('GQE', 'GQE'), ('GNS', 'GNS'), ('JMD', 'JMD'), ('RWF', 'RWF'), ('XEU', 'XEU'), ('TZS', 'TZS'), ('FKP', 'FKP'), ('BND', 'BND'), ('MOP', 'MOP'), ('HUF', 'HUF'), ('MVR', 'MVR'), ('UYW', 'UYW'), ('PES', 'PES'), ('SBD', 'SBD'), ('XBD', 'XBD'), ('NLG', 'NLG'), ('HKD', 'HKD'), ('BEF', 'BEF'), ('SIT', 'SIT'), ('MZE', 'MZE'), ('AUD', 'AUD'), ('ZWR', 'ZWR'), ('PLZ', 'PLZ'), ('LRD', 'LRD'), ('BZD', 'BZD'), ('LSL', 'LSL'), ('SKK', 'SKK'), ('XAF', 'XAF'), ('NIC', 'NIC'), ('XCD', 'XCD'), ('XPT', 'XPT'), ('UYP', 'UYP'), ('XOF', 'XOF'), ('YUM', 'YUM'), ('DEM', 'DEM'), ('AOR', 'AOR'), ('CLE', 'CLE'), ('TJR', 'TJR'), ('UAH', 'UAH'), ('ROL', 'ROL'), ('AMD', 'AMD'), ('CVE', 'CVE'), ('COU', 'COU'), ('BYB', 'BYB'), ('DZD', 'DZD'), ('ADP', 'ADP'), ('YDD', 'YDD'), ('BMD', 'BMD'), ('ILS', 'ILS'), ('BRZ', 'BRZ'), ('STN', 'STN'), ('BGM', 'BGM'), ('PGK', 'PGK'), ('RHD', 'RHD'), ('BRB', 'BRB'), ('KRW', 'KRW'), ('CAD', 'CAD'), ('RUB', 'RUB'), ('KPW', 'KPW'), ('SDD', 'SDD'), ('ZAR', 'ZAR'), ('XBB', 'XBB'), ('SRD', 'SRD'), ('BYN', 'BYN'), ('ERN', 'ERN'), ('MKD', 'MKD'), ('SLL', 'SLL'), ('BOP', 'BOP'), ('BGO', 'BGO'), ('ISJ', 'ISJ'), ('TRL', 'TRL'), ('JOD', 'JOD'), ('GHC', 'GHC'), ('NZD', 'NZD'), ('XAU', 'XAU'), ('IDR', 'IDR'), ('MZN', 'MZN'), ('XTS', 'XTS'), ('DJF', 'DJF'), ('KRO', 'KRO'), ('XAG', 'XAG'), ('MUR', 'MUR'), ('SCR', 'SCR'), ('SHP', 'SHP'), ('USN', 'USN'), ('BBD', 'BBD'), ('XPD', 'XPD'), ('SRG', 'SRG'), ('XXX', 'XXX'), ('MNT', 'MNT'), ('CNX', 'CNX'), ('AOA', 'AOA'), ('CUC', 'CUC'), ('TMM', 'TMM'), ('TND', 'TND'), ('AFA', 'AFA'), ('JPY', 'JPY'), ('GYD', 'GYD'), ('XSU', 'XSU'), ('BOV', 'BOV'), ('KWD', 'KWD'), ('KES', 'KES'), ('BWP', 'BWP'), ('CYP', 'CYP'), ('USD', 'USD'), ('PAB', 'PAB'), ('DOP', 'DOP'), ('LUF', 'LUF'), ('BSD', 'BSD'), ('SVC', 'SVC'), ('YUN', 'YUN'), ('GEK', 'GEK'), ('XBA', 'XBA'), ('PKR', 'PKR'), ('CDF', 'CDF'), ('IEP', 'IEP'), ('BHD', 'BHD'), ('BGN', 'BGN'), ('MXP', 'MXP'), ('PTE', 'PTE'), ('AWG', 'AWG'), ('MDC', 'MDC'), ('MAD', 'MAD'), ('CHW', 'CHW'), ('ILR', 'ILR'), ('SEK', 'SEK'), ('ECS', 'ECS'), ('ALL', 'ALL'), ('DKK', 'DKK'), ('TWD', 'TWD'), ('UZS', 'UZS'), ('LBP', 'LBP'), ('LTL', 'LTL'), ('UGS', 'UGS'), ('WST', 'WST'), ('RUR', 'RUR')], max_length=100),
        ),
    ]
