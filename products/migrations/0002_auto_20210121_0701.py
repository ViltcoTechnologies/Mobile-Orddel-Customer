# Generated by Django 3.1.4 on 2021-01-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('ERN', 'ERN'), ('PYG', 'PYG'), ('KYD', 'KYD'), ('BAM', 'BAM'), ('XAF', 'XAF'), ('BEC', 'BEC'), ('KMF', 'KMF'), ('PTE', 'PTE'), ('XOF', 'XOF'), ('DDM', 'DDM'), ('KHR', 'KHR'), ('MZE', 'MZE'), ('SOS', 'SOS'), ('COP', 'COP'), ('AWG', 'AWG'), ('BGL', 'BGL'), ('ZRZ', 'ZRZ'), ('MNT', 'MNT'), ('SUR', 'SUR'), ('CHW', 'CHW'), ('XTS', 'XTS'), ('CVE', 'CVE'), ('UYP', 'UYP'), ('AED', 'AED'), ('BMD', 'BMD'), ('GEK', 'GEK'), ('SBD', 'SBD'), ('IDR', 'IDR'), ('SKK', 'SKK'), ('ALL', 'ALL'), ('CUC', 'CUC'), ('BZD', 'BZD'), ('HKD', 'HKD'), ('SZL', 'SZL'), ('ARM', 'ARM'), ('SGD', 'SGD'), ('JOD', 'JOD'), ('TZS', 'TZS'), ('UAK', 'UAK'), ('SDG', 'SDG'), ('XAG', 'XAG'), ('IRR', 'IRR'), ('IEP', 'IEP'), ('SVC', 'SVC'), ('MTP', 'MTP'), ('BGM', 'BGM'), ('MAF', 'MAF'), ('HUF', 'HUF'), ('BUK', 'BUK'), ('XEU', 'XEU'), ('GHC', 'GHC'), ('PGK', 'PGK'), ('BEL', 'BEL'), ('ZWL', 'ZWL'), ('ETB', 'ETB'), ('USD', 'USD'), ('AZN', 'AZN'), ('TRY', 'TRY'), ('TWD', 'TWD'), ('KRW', 'KRW'), ('MZN', 'MZN'), ('BBD', 'BBD'), ('ROL', 'ROL'), ('LBP', 'LBP'), ('BRN', 'BRN'), ('NOK', 'NOK'), ('GTQ', 'GTQ'), ('CHF', 'CHF'), ('ZRN', 'ZRN'), ('GIP', 'GIP'), ('XAU', 'XAU'), ('XPT', 'XPT'), ('BIF', 'BIF'), ('MRO', 'MRO'), ('GNS', 'GNS'), ('LAK', 'LAK'), ('XRE', 'XRE'), ('AZM', 'AZM'), ('RWF', 'RWF'), ('IQD', 'IQD'), ('XBA', 'XBA'), ('GQE', 'GQE'), ('XBB', 'XBB'), ('CRC', 'CRC'), ('ARP', 'ARP'), ('XBC', 'XBC'), ('SEK', 'SEK'), ('LUL', 'LUL'), ('PHP', 'PHP'), ('THB', 'THB'), ('TJS', 'TJS'), ('COU', 'COU'), ('MGA', 'MGA'), ('GRD', 'GRD'), ('SAR', 'SAR'), ('CLF', 'CLF'), ('XSU', 'XSU'), ('MLF', 'MLF'), ('BOL', 'BOL'), ('INR', 'INR'), ('JMD', 'JMD'), ('MKN', 'MKN'), ('SIT', 'SIT'), ('YUN', 'YUN'), ('XUA', 'XUA'), ('BDT', 'BDT'), ('TTD', 'TTD'), ('CLP', 'CLP'), ('EEK', 'EEK'), ('HRD', 'HRD'), ('LYD', 'LYD'), ('ADP', 'ADP'), ('AFA', 'AFA'), ('MXN', 'MXN'), ('ITL', 'ITL'), ('MCF', 'MCF'), ('TOP', 'TOP'), ('AMD', 'AMD'), ('ZAR', 'ZAR'), ('TMT', 'TMT'), ('XFO', 'XFO'), ('YUD', 'YUD'), ('YER', 'YER'), ('JPY', 'JPY'), ('VEB', 'VEB'), ('KGS', 'KGS'), ('GMD', 'GMD'), ('NLG', 'NLG'), ('ECV', 'ECV'), ('MTL', 'MTL'), ('RON', 'RON'), ('CHE', 'CHE'), ('BRL', 'BRL'), ('ESB', 'ESB'), ('BSD', 'BSD'), ('STD', 'STD'), ('MZM', 'MZM'), ('OMR', 'OMR'), ('FRF', 'FRF'), ('NPR', 'NPR'), ('LRD', 'LRD'), ('XCD', 'XCD'), ('BRB', 'BRB'), ('UAH', 'UAH'), ('WST', 'WST'), ('AOA', 'AOA'), ('BAN', 'BAN'), ('SDP', 'SDP'), ('MVR', 'MVR'), ('ZWD', 'ZWD'), ('BOV', 'BOV'), ('MUR', 'MUR'), ('CNX', 'CNX'), ('LTT', 'LTT'), ('ARL', 'ARL'), ('DOP', 'DOP'), ('GWE', 'GWE'), ('SHP', 'SHP'), ('GEL', 'GEL'), ('BOP', 'BOP'), ('KPW', 'KPW'), ('SYP', 'SYP'), ('USS', 'USS'), ('TRL', 'TRL'), ('BTN', 'BTN'), ('CAD', 'CAD'), ('FJD', 'FJD'), ('SCR', 'SCR'), ('KRO', 'KRO'), ('ILS', 'ILS'), ('LVL', 'LVL'), ('MRU', 'MRU'), ('CLE', 'CLE'), ('BEF', 'BEF'), ('PKR', 'PKR'), ('GYD', 'GYD'), ('PEN', 'PEN'), ('BYN', 'BYN'), ('SSP', 'SSP'), ('DEM', 'DEM'), ('MAD', 'MAD'), ('DZD', 'DZD'), ('LUC', 'LUC'), ('UYU', 'UYU'), ('FIM', 'FIM'), ('PES', 'PES'), ('DJF', 'DJF'), ('VES', 'VES'), ('RSD', 'RSD'), ('BRR', 'BRR'), ('LTL', 'LTL'), ('ATS', 'ATS'), ('KRH', 'KRH'), ('ANG', 'ANG'), ('CSD', 'CSD'), ('GHS', 'GHS'), ('LVR', 'LVR'), ('AOK', 'AOK'), ('BHD', 'BHD'), ('EUR', 'EUR'), ('CNY', 'CNY'), ('MXP', 'MXP'), ('UGX', 'UGX'), ('MDL', 'MDL'), ('BAD', 'BAD'), ('HNL', 'HNL'), ('KWD', 'KWD'), ('BGN', 'BGN'), ('ZMW', 'ZMW'), ('BND', 'BND'), ('PEI', 'PEI'), ('CZK', 'CZK'), ('ILP', 'ILP'), ('ARS', 'ARS'), ('AFN', 'AFN'), ('HTG', 'HTG'), ('QAR', 'QAR'), ('CNH', 'CNH'), ('MMK', 'MMK'), ('VND', 'VND'), ('MYR', 'MYR'), ('BYR', 'BYR'), ('LUF', 'LUF'), ('XFU', 'XFU'), ('CUP', 'CUP'), ('BYB', 'BYB'), ('NIC', 'NIC'), ('AON', 'AON'), ('SDD', 'SDD'), ('UGS', 'UGS'), ('ILR', 'ILR'), ('YUM', 'YUM'), ('UZS', 'UZS'), ('BRZ', 'BRZ'), ('SRG', 'SRG'), ('MVP', 'MVP'), ('AOR', 'AOR'), ('YUR', 'YUR'), ('BRE', 'BRE'), ('VNN', 'VNN'), ('NZD', 'NZD'), ('FKP', 'FKP'), ('KES', 'KES'), ('XPF', 'XPF'), ('GNF', 'GNF'), ('AUD', 'AUD'), ('XPD', 'XPD'), ('ZWR', 'ZWR'), ('NAD', 'NAD'), ('ISK', 'ISK'), ('MDC', 'MDC'), ('HRK', 'HRK'), ('MWK', 'MWK'), ('TPE', 'TPE'), ('XXX', 'XXX'), ('RHD', 'RHD'), ('RUB', 'RUB'), ('SRD', 'SRD'), ('ESA', 'ESA'), ('BRC', 'BRC'), ('UYI', 'UYI'), ('USN', 'USN'), ('VEF', 'VEF'), ('VUV', 'VUV'), ('ISJ', 'ISJ'), ('NIO', 'NIO'), ('XBD', 'XBD'), ('DKK', 'DKK'), ('CYP', 'CYP'), ('ECS', 'ECS'), ('PLN', 'PLN'), ('PLZ', 'PLZ'), ('EGP', 'EGP'), ('GWP', 'GWP'), ('TND', 'TND'), ('CDF', 'CDF'), ('NGN', 'NGN'), ('XDR', 'XDR'), ('TMM', 'TMM'), ('CSK', 'CSK'), ('BGO', 'BGO'), ('BWP', 'BWP'), ('SLL', 'SLL'), ('STN', 'STN'), ('YDD', 'YDD'), ('UYW', 'UYW'), ('ESP', 'ESP'), ('BOB', 'BOB'), ('PAB', 'PAB'), ('ZMK', 'ZMK'), ('LSL', 'LSL'), ('KZT', 'KZT'), ('MOP', 'MOP'), ('ZAL', 'ZAL'), ('TJR', 'TJR'), ('LKR', 'LKR'), ('ARA', 'ARA'), ('GBP', 'GBP'), ('MGF', 'MGF'), ('MXV', 'MXV'), ('ALK', 'ALK'), ('RUR', 'RUR'), ('MKD', 'MKD')], max_length=100),
        ),
    ]
