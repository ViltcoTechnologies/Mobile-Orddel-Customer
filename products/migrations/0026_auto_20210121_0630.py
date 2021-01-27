# Generated by Django 3.1.5 on 2021-01-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20210121_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('MGA', 'MGA'), ('PGK', 'PGK'), ('UZS', 'UZS'), ('DDM', 'DDM'), ('MRU', 'MRU'), ('YDD', 'YDD'), ('DZD', 'DZD'), ('ARL', 'ARL'), ('AZN', 'AZN'), ('VEF', 'VEF'), ('MOP', 'MOP'), ('XDR', 'XDR'), ('ESB', 'ESB'), ('MRO', 'MRO'), ('ZWD', 'ZWD'), ('GHS', 'GHS'), ('USN', 'USN'), ('AOK', 'AOK'), ('MXV', 'MXV'), ('BAD', 'BAD'), ('SVC', 'SVC'), ('CHF', 'CHF'), ('GIP', 'GIP'), ('BRE', 'BRE'), ('ERN', 'ERN'), ('MVP', 'MVP'), ('SDD', 'SDD'), ('BAN', 'BAN'), ('CZK', 'CZK'), ('YUR', 'YUR'), ('CSD', 'CSD'), ('ZRZ', 'ZRZ'), ('PHP', 'PHP'), ('GHC', 'GHC'), ('PTE', 'PTE'), ('GNF', 'GNF'), ('XFO', 'XFO'), ('TRY', 'TRY'), ('CHE', 'CHE'), ('SKK', 'SKK'), ('TTD', 'TTD'), ('EEK', 'EEK'), ('MXP', 'MXP'), ('UGS', 'UGS'), ('HNL', 'HNL'), ('GTQ', 'GTQ'), ('BGO', 'BGO'), ('QAR', 'QAR'), ('HKD', 'HKD'), ('KGS', 'KGS'), ('LKR', 'LKR'), ('UYP', 'UYP'), ('CYP', 'CYP'), ('NZD', 'NZD'), ('ILS', 'ILS'), ('XAF', 'XAF'), ('MZM', 'MZM'), ('PLN', 'PLN'), ('ARA', 'ARA'), ('TPE', 'TPE'), ('ALL', 'ALL'), ('MUR', 'MUR'), ('SLL', 'SLL'), ('VES', 'VES'), ('ATS', 'ATS'), ('MMK', 'MMK'), ('MZN', 'MZN'), ('BDT', 'BDT'), ('XCD', 'XCD'), ('ZAR', 'ZAR'), ('UAH', 'UAH'), ('ECS', 'ECS'), ('ZWR', 'ZWR'), ('XBB', 'XBB'), ('BMD', 'BMD'), ('BBD', 'BBD'), ('CSK', 'CSK'), ('IEP', 'IEP'), ('ZMK', 'ZMK'), ('SCR', 'SCR'), ('KWD', 'KWD'), ('NLG', 'NLG'), ('DOP', 'DOP'), ('BSD', 'BSD'), ('AOR', 'AOR'), ('SGD', 'SGD'), ('XPD', 'XPD'), ('FKP', 'FKP'), ('CLP', 'CLP'), ('XAU', 'XAU'), ('KMF', 'KMF'), ('XEU', 'XEU'), ('BYN', 'BYN'), ('LSL', 'LSL'), ('XPF', 'XPF'), ('GBP', 'GBP'), ('SHP', 'SHP'), ('DJF', 'DJF'), ('KRW', 'KRW'), ('LVR', 'LVR'), ('ISJ', 'ISJ'), ('CAD', 'CAD'), ('ILP', 'ILP'), ('LVL', 'LVL'), ('SRD', 'SRD'), ('STD', 'STD'), ('ARM', 'ARM'), ('GQE', 'GQE'), ('BRC', 'BRC'), ('GNS', 'GNS'), ('BUK', 'BUK'), ('BTN', 'BTN'), ('CLE', 'CLE'), ('XTS', 'XTS'), ('UYW', 'UYW'), ('BRZ', 'BRZ'), ('ARS', 'ARS'), ('LAK', 'LAK'), ('TJR', 'TJR'), ('PKR', 'PKR'), ('AZM', 'AZM'), ('MXN', 'MXN'), ('GYD', 'GYD'), ('EUR', 'EUR'), ('PYG', 'PYG'), ('LYD', 'LYD'), ('JPY', 'JPY'), ('ESA', 'ESA'), ('BOV', 'BOV'), ('LUC', 'LUC'), ('CUC', 'CUC'), ('RUR', 'RUR'), ('UYU', 'UYU'), ('FIM', 'FIM'), ('YER', 'YER'), ('BOP', 'BOP'), ('VUV', 'VUV'), ('XFU', 'XFU'), ('USS', 'USS'), ('BRB', 'BRB'), ('CDF', 'CDF'), ('LTL', 'LTL'), ('RON', 'RON'), ('XPT', 'XPT'), ('BRN', 'BRN'), ('XSU', 'XSU'), ('GEL', 'GEL'), ('GWE', 'GWE'), ('FRF', 'FRF'), ('CHW', 'CHW'), ('AUD', 'AUD'), ('GMD', 'GMD'), ('PEI', 'PEI'), ('BWP', 'BWP'), ('PLZ', 'PLZ'), ('ROL', 'ROL'), ('MDC', 'MDC'), ('ILR', 'ILR'), ('YUN', 'YUN'), ('RWF', 'RWF'), ('VND', 'VND'), ('IQD', 'IQD'), ('KES', 'KES'), ('CNX', 'CNX'), ('CLF', 'CLF'), ('RUB', 'RUB'), ('BHD', 'BHD'), ('XRE', 'XRE'), ('MCF', 'MCF'), ('SZL', 'SZL'), ('LUL', 'LUL'), ('SDP', 'SDP'), ('AMD', 'AMD'), ('CVE', 'CVE'), ('RSD', 'RSD'), ('ITL', 'ITL'), ('ADP', 'ADP'), ('USD', 'USD'), ('BEL', 'BEL'), ('ESP', 'ESP'), ('KZT', 'KZT'), ('INR', 'INR'), ('XOF', 'XOF'), ('DEM', 'DEM'), ('MAF', 'MAF'), ('MLF', 'MLF'), ('GWP', 'GWP'), ('BGL', 'BGL'), ('LBP', 'LBP'), ('HTG', 'HTG'), ('TMM', 'TMM'), ('OMR', 'OMR'), ('BEF', 'BEF'), ('XXX', 'XXX'), ('ZWL', 'ZWL'), ('BOL', 'BOL'), ('PES', 'PES'), ('MKD', 'MKD'), ('SDG', 'SDG'), ('PAB', 'PAB'), ('XAG', 'XAG'), ('MAD', 'MAD'), ('SEK', 'SEK'), ('ZAL', 'ZAL'), ('AOA', 'AOA'), ('EGP', 'EGP'), ('SYP', 'SYP'), ('TZS', 'TZS'), ('COU', 'COU'), ('STN', 'STN'), ('TND', 'TND'), ('SIT', 'SIT'), ('BEC', 'BEC'), ('HUF', 'HUF'), ('TOP', 'TOP'), ('NGN', 'NGN'), ('VNN', 'VNN'), ('UAK', 'UAK'), ('BRR', 'BRR'), ('GRD', 'GRD'), ('NPR', 'NPR'), ('LRD', 'LRD'), ('AON', 'AON'), ('ETB', 'ETB'), ('SBD', 'SBD'), ('TRL', 'TRL'), ('BZD', 'BZD'), ('IRR', 'IRR'), ('BIF', 'BIF'), ('AWG', 'AWG'), ('ZRN', 'ZRN'), ('THB', 'THB'), ('AFN', 'AFN'), ('AED', 'AED'), ('MTP', 'MTP'), ('JMD', 'JMD'), ('ZMW', 'ZMW'), ('XBA', 'XBA'), ('JOD', 'JOD'), ('SOS', 'SOS'), ('NIC', 'NIC'), ('FJD', 'FJD'), ('XBC', 'XBC'), ('VEB', 'VEB'), ('TWD', 'TWD'), ('XUA', 'XUA'), ('BYB', 'BYB'), ('MGF', 'MGF'), ('MNT', 'MNT'), ('WST', 'WST'), ('TMT', 'TMT'), ('NAD', 'NAD'), ('MTL', 'MTL'), ('BGM', 'BGM'), ('IDR', 'IDR'), ('MZE', 'MZE'), ('PEN', 'PEN'), ('GEK', 'GEK'), ('NIO', 'NIO'), ('ALK', 'ALK'), ('KRO', 'KRO'), ('MDL', 'MDL'), ('YUD', 'YUD'), ('RHD', 'RHD'), ('LUF', 'LUF'), ('UYI', 'UYI'), ('COP', 'COP'), ('DKK', 'DKK'), ('KPW', 'KPW'), ('ISK', 'ISK'), ('MYR', 'MYR'), ('MKN', 'MKN'), ('NOK', 'NOK'), ('SUR', 'SUR'), ('CNH', 'CNH'), ('KRH', 'KRH'), ('ARP', 'ARP'), ('MVR', 'MVR'), ('SAR', 'SAR'), ('TJS', 'TJS'), ('UGX', 'UGX'), ('ANG', 'ANG'), ('CNY', 'CNY'), ('BYR', 'BYR'), ('LTT', 'LTT'), ('ECV', 'ECV'), ('HRD', 'HRD'), ('XBD', 'XBD'), ('BGN', 'BGN'), ('YUM', 'YUM'), ('SSP', 'SSP'), ('SRG', 'SRG'), ('BRL', 'BRL'), ('KYD', 'KYD'), ('CRC', 'CRC'), ('BOB', 'BOB'), ('KHR', 'KHR'), ('BND', 'BND'), ('CUP', 'CUP'), ('BAM', 'BAM'), ('HRK', 'HRK'), ('MWK', 'MWK'), ('AFA', 'AFA')], max_length=100),
        ),
    ]
