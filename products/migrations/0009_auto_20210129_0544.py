# Generated by Django 3.1.4 on 2021-01-29 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210129_0543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('ZWD', 'ZWD'), ('CYP', 'CYP'), ('XBB', 'XBB'), ('XPT', 'XPT'), ('RUR', 'RUR'), ('AOK', 'AOK'), ('DZD', 'DZD'), ('PEN', 'PEN'), ('SKK', 'SKK'), ('USN', 'USN'), ('UYP', 'UYP'), ('PLZ', 'PLZ'), ('EEK', 'EEK'), ('KES', 'KES'), ('GEL', 'GEL'), ('CLE', 'CLE'), ('AFA', 'AFA'), ('TJR', 'TJR'), ('ZMK', 'ZMK'), ('MYR', 'MYR'), ('GEK', 'GEK'), ('BGL', 'BGL'), ('XEU', 'XEU'), ('MXV', 'MXV'), ('AED', 'AED'), ('KRH', 'KRH'), ('SCR', 'SCR'), ('LSL', 'LSL'), ('VES', 'VES'), ('JMD', 'JMD'), ('PLN', 'PLN'), ('RON', 'RON'), ('XCD', 'XCD'), ('DEM', 'DEM'), ('HRK', 'HRK'), ('IEP', 'IEP'), ('CHW', 'CHW'), ('XAF', 'XAF'), ('ARM', 'ARM'), ('DOP', 'DOP'), ('MVP', 'MVP'), ('BUK', 'BUK'), ('BOB', 'BOB'), ('BND', 'BND'), ('UYI', 'UYI'), ('ILP', 'ILP'), ('GRD', 'GRD'), ('BMD', 'BMD'), ('BYB', 'BYB'), ('DDM', 'DDM'), ('XAU', 'XAU'), ('JPY', 'JPY'), ('UYW', 'UYW'), ('MAF', 'MAF'), ('LUL', 'LUL'), ('MGA', 'MGA'), ('ZWL', 'ZWL'), ('XBD', 'XBD'), ('SAR', 'SAR'), ('TJS', 'TJS'), ('BEF', 'BEF'), ('ECV', 'ECV'), ('CHF', 'CHF'), ('HUF', 'HUF'), ('MAD', 'MAD'), ('QAR', 'QAR'), ('BWP', 'BWP'), ('BAN', 'BAN'), ('BGM', 'BGM'), ('VUV', 'VUV'), ('NPR', 'NPR'), ('AUD', 'AUD'), ('SVC', 'SVC'), ('AZN', 'AZN'), ('CAD', 'CAD'), ('GBP', 'GBP'), ('ARS', 'ARS'), ('BGN', 'BGN'), ('YDD', 'YDD'), ('HTG', 'HTG'), ('LVL', 'LVL'), ('RWF', 'RWF'), ('SDD', 'SDD'), ('GNF', 'GNF'), ('UAH', 'UAH'), ('OMR', 'OMR'), ('MRO', 'MRO'), ('XSU', 'XSU'), ('UGX', 'UGX'), ('GYD', 'GYD'), ('UZS', 'UZS'), ('GNS', 'GNS'), ('SUR', 'SUR'), ('FKP', 'FKP'), ('GWE', 'GWE'), ('ISJ', 'ISJ'), ('BEL', 'BEL'), ('AOA', 'AOA'), ('TMM', 'TMM'), ('AWG', 'AWG'), ('NZD', 'NZD'), ('NAD', 'NAD'), ('MTP', 'MTP'), ('BYR', 'BYR'), ('KGS', 'KGS'), ('GIP', 'GIP'), ('MRU', 'MRU'), ('XPD', 'XPD'), ('BRB', 'BRB'), ('SZL', 'SZL'), ('ZRZ', 'ZRZ'), ('MDL', 'MDL'), ('GTQ', 'GTQ'), ('COU', 'COU'), ('SHP', 'SHP'), ('PAB', 'PAB'), ('TRY', 'TRY'), ('XBA', 'XBA'), ('SBD', 'SBD'), ('NLG', 'NLG'), ('ANG', 'ANG'), ('RUB', 'RUB'), ('CZK', 'CZK'), ('BZD', 'BZD'), ('LKR', 'LKR'), ('MNT', 'MNT'), ('ZRN', 'ZRN'), ('KHR', 'KHR'), ('ARL', 'ARL'), ('AON', 'AON'), ('MLF', 'MLF'), ('AOR', 'AOR'), ('MVR', 'MVR'), ('ADP', 'ADP'), ('YUR', 'YUR'), ('YER', 'YER'), ('PTE', 'PTE'), ('ATS', 'ATS'), ('IDR', 'IDR'), ('PGK', 'PGK'), ('SIT', 'SIT'), ('EUR', 'EUR'), ('MXN', 'MXN'), ('AFN', 'AFN'), ('MTL', 'MTL'), ('ESA', 'ESA'), ('BOV', 'BOV'), ('MXP', 'MXP'), ('XXX', 'XXX'), ('BTN', 'BTN'), ('ZAL', 'ZAL'), ('CDF', 'CDF'), ('XUA', 'XUA'), ('NGN', 'NGN'), ('MOP', 'MOP'), ('NIC', 'NIC'), ('DJF', 'DJF'), ('ZAR', 'ZAR'), ('SEK', 'SEK'), ('ESB', 'ESB'), ('LRD', 'LRD'), ('XFU', 'XFU'), ('BGO', 'BGO'), ('XOF', 'XOF'), ('TZS', 'TZS'), ('VEB', 'VEB'), ('GMD', 'GMD'), ('KZT', 'KZT'), ('BIF', 'BIF'), ('FIM', 'FIM'), ('NIO', 'NIO'), ('BDT', 'BDT'), ('KWD', 'KWD'), ('ITL', 'ITL'), ('LYD', 'LYD'), ('SRD', 'SRD'), ('UGS', 'UGS'), ('SSP', 'SSP'), ('USD', 'USD'), ('MZN', 'MZN'), ('CNX', 'CNX'), ('MDC', 'MDC'), ('VEF', 'VEF'), ('ERN', 'ERN'), ('IRR', 'IRR'), ('YUD', 'YUD'), ('MKN', 'MKN'), ('TPE', 'TPE'), ('ARA', 'ARA'), ('USS', 'USS'), ('SDP', 'SDP'), ('BRE', 'BRE'), ('SGD', 'SGD'), ('LUF', 'LUF'), ('ISK', 'ISK'), ('GQE', 'GQE'), ('DKK', 'DKK'), ('MZM', 'MZM'), ('HRD', 'HRD'), ('PYG', 'PYG'), ('SRG', 'SRG'), ('VND', 'VND'), ('CUC', 'CUC'), ('PEI', 'PEI'), ('ECS', 'ECS'), ('XAG', 'XAG'), ('HKD', 'HKD'), ('AMD', 'AMD'), ('FJD', 'FJD'), ('MCF', 'MCF'), ('MKD', 'MKD'), ('GHS', 'GHS'), ('LTL', 'LTL'), ('KRW', 'KRW'), ('RHD', 'RHD'), ('GWP', 'GWP'), ('TRL', 'TRL'), ('KRO', 'KRO'), ('BRL', 'BRL'), ('VNN', 'VNN'), ('KMF', 'KMF'), ('XPF', 'XPF'), ('CSD', 'CSD'), ('ALK', 'ALK'), ('UYU', 'UYU'), ('BYN', 'BYN'), ('BAM', 'BAM'), ('TMT', 'TMT'), ('SOS', 'SOS'), ('CVE', 'CVE'), ('XTS', 'XTS'), ('CNY', 'CNY'), ('KYD', 'KYD'), ('ROL', 'ROL'), ('UAK', 'UAK'), ('EGP', 'EGP'), ('BOP', 'BOP'), ('LBP', 'LBP'), ('ZWR', 'ZWR'), ('THB', 'THB'), ('KPW', 'KPW'), ('INR', 'INR'), ('ESP', 'ESP'), ('CSK', 'CSK'), ('AZM', 'AZM'), ('BOL', 'BOL'), ('SDG', 'SDG'), ('ZMW', 'ZMW'), ('YUN', 'YUN'), ('COP', 'COP'), ('IQD', 'IQD'), ('TOP', 'TOP'), ('ETB', 'ETB'), ('BBD', 'BBD'), ('YUM', 'YUM'), ('NOK', 'NOK'), ('BRZ', 'BRZ'), ('MWK', 'MWK'), ('SYP', 'SYP'), ('BRR', 'BRR'), ('CHE', 'CHE'), ('LAK', 'LAK'), ('PES', 'PES'), ('MZE', 'MZE'), ('TTD', 'TTD'), ('CNH', 'CNH'), ('HNL', 'HNL'), ('BAD', 'BAD'), ('BEC', 'BEC'), ('JOD', 'JOD'), ('GHC', 'GHC'), ('CLP', 'CLP'), ('ALL', 'ALL'), ('BRN', 'BRN'), ('XBC', 'XBC'), ('FRF', 'FRF'), ('STD', 'STD'), ('PKR', 'PKR'), ('BRC', 'BRC'), ('SLL', 'SLL'), ('WST', 'WST'), ('RSD', 'RSD'), ('CUP', 'CUP'), ('ARP', 'ARP'), ('TND', 'TND'), ('ILR', 'ILR'), ('LUC', 'LUC'), ('BSD', 'BSD'), ('MUR', 'MUR'), ('LTT', 'LTT'), ('LVR', 'LVR'), ('TWD', 'TWD'), ('XRE', 'XRE'), ('ILS', 'ILS'), ('CLF', 'CLF'), ('STN', 'STN'), ('MMK', 'MMK'), ('XFO', 'XFO'), ('PHP', 'PHP'), ('MGF', 'MGF'), ('CRC', 'CRC'), ('XDR', 'XDR'), ('BHD', 'BHD')], max_length=100),
        ),
    ]
