# Generated by Django 3.1.4 on 2021-01-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210114_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(choices=[('TTD', 'TTD'), ('SVC', 'SVC'), ('GEL', 'GEL'), ('VNN', 'VNN'), ('ANG', 'ANG'), ('PES', 'PES'), ('CVE', 'CVE'), ('LSL', 'LSL'), ('VUV', 'VUV'), ('COP', 'COP'), ('PAB', 'PAB'), ('TJR', 'TJR'), ('DOP', 'DOP'), ('MVR', 'MVR'), ('VND', 'VND'), ('RHD', 'RHD'), ('HRK', 'HRK'), ('CUC', 'CUC'), ('ROL', 'ROL'), ('ATS', 'ATS'), ('ESP', 'ESP'), ('TRL', 'TRL'), ('MGA', 'MGA'), ('UYW', 'UYW'), ('INR', 'INR'), ('BMD', 'BMD'), ('GHC', 'GHC'), ('BUK', 'BUK'), ('ALL', 'ALL'), ('TRY', 'TRY'), ('DZD', 'DZD'), ('MYR', 'MYR'), ('ECS', 'ECS'), ('BOL', 'BOL'), ('BYN', 'BYN'), ('GWE', 'GWE'), ('MXV', 'MXV'), ('BYR', 'BYR'), ('BSD', 'BSD'), ('UAK', 'UAK'), ('CLP', 'CLP'), ('USD', 'USD'), ('BGN', 'BGN'), ('LBP', 'LBP'), ('CLF', 'CLF'), ('LTT', 'LTT'), ('KRW', 'KRW'), ('SHP', 'SHP'), ('CSK', 'CSK'), ('ESA', 'ESA'), ('BGL', 'BGL'), ('SUR', 'SUR'), ('IQD', 'IQD'), ('WST', 'WST'), ('MLF', 'MLF'), ('CNH', 'CNH'), ('SDG', 'SDG'), ('SIT', 'SIT'), ('FJD', 'FJD'), ('KES', 'KES'), ('RUB', 'RUB'), ('SLL', 'SLL'), ('UYU', 'UYU'), ('DJF', 'DJF'), ('IRR', 'IRR'), ('CNY', 'CNY'), ('GNS', 'GNS'), ('ESB', 'ESB'), ('LKR', 'LKR'), ('SCR', 'SCR'), ('LUL', 'LUL'), ('AON', 'AON'), ('MRO', 'MRO'), ('LTL', 'LTL'), ('CHW', 'CHW'), ('OMR', 'OMR'), ('BRL', 'BRL'), ('MUR', 'MUR'), ('RSD', 'RSD'), ('TJS', 'TJS'), ('ALK', 'ALK'), ('AFA', 'AFA'), ('CNX', 'CNX'), ('KHR', 'KHR'), ('DKK', 'DKK'), ('DDM', 'DDM'), ('LVL', 'LVL'), ('GQE', 'GQE'), ('CLE', 'CLE'), ('SGD', 'SGD'), ('GTQ', 'GTQ'), ('STD', 'STD'), ('NAD', 'NAD'), ('CDF', 'CDF'), ('KRH', 'KRH'), ('ZMW', 'ZMW'), ('GWP', 'GWP'), ('NZD', 'NZD'), ('ETB', 'ETB'), ('UZS', 'UZS'), ('IEP', 'IEP'), ('KZT', 'KZT'), ('LVR', 'LVR'), ('TMM', 'TMM'), ('TND', 'TND'), ('BYB', 'BYB'), ('HKD', 'HKD'), ('XBD', 'XBD'), ('XAF', 'XAF'), ('YUR', 'YUR'), ('GHS', 'GHS'), ('IDR', 'IDR'), ('MTL', 'MTL'), ('ARS', 'ARS'), ('AUD', 'AUD'), ('EEK', 'EEK'), ('USS', 'USS'), ('RON', 'RON'), ('AMD', 'AMD'), ('BRZ', 'BRZ'), ('ILS', 'ILS'), ('ZWR', 'ZWR'), ('BND', 'BND'), ('XCD', 'XCD'), ('HRD', 'HRD'), ('MXN', 'MXN'), ('LAK', 'LAK'), ('EGP', 'EGP'), ('XTS', 'XTS'), ('XAG', 'XAG'), ('MAD', 'MAD'), ('CSD', 'CSD'), ('LUF', 'LUF'), ('TOP', 'TOP'), ('PKR', 'PKR'), ('ITL', 'ITL'), ('YUM', 'YUM'), ('MDC', 'MDC'), ('PYG', 'PYG'), ('CRC', 'CRC'), ('PGK', 'PGK'), ('XOF', 'XOF'), ('USN', 'USN'), ('NIC', 'NIC'), ('VES', 'VES'), ('SRD', 'SRD'), ('XDR', 'XDR'), ('CYP', 'CYP'), ('BOB', 'BOB'), ('VEB', 'VEB'), ('SOS', 'SOS'), ('ZRN', 'ZRN'), ('RUR', 'RUR'), ('ARA', 'ARA'), ('AOK', 'AOK'), ('UYP', 'UYP'), ('MWK', 'MWK'), ('XFU', 'XFU'), ('SDP', 'SDP'), ('THB', 'THB'), ('BIF', 'BIF'), ('BRE', 'BRE'), ('MGF', 'MGF'), ('YUD', 'YUD'), ('TZS', 'TZS'), ('MXP', 'MXP'), ('BRB', 'BRB'), ('SAR', 'SAR'), ('GYD', 'GYD'), ('PTE', 'PTE'), ('BTN', 'BTN'), ('BRC', 'BRC'), ('TPE', 'TPE'), ('BZD', 'BZD'), ('TMT', 'TMT'), ('BGO', 'BGO'), ('AED', 'AED'), ('AOR', 'AOR'), ('PEI', 'PEI'), ('AFN', 'AFN'), ('BEF', 'BEF'), ('MTP', 'MTP'), ('SRG', 'SRG'), ('YUN', 'YUN'), ('KRO', 'KRO'), ('JMD', 'JMD'), ('GEK', 'GEK'), ('CUP', 'CUP'), ('NGN', 'NGN'), ('COU', 'COU'), ('NOK', 'NOK'), ('STN', 'STN'), ('HUF', 'HUF'), ('TWD', 'TWD'), ('UGS', 'UGS'), ('FRF', 'FRF'), ('AWG', 'AWG'), ('MKD', 'MKD'), ('KMF', 'KMF'), ('PLN', 'PLN'), ('HTG', 'HTG'), ('MZE', 'MZE'), ('XBB', 'XBB'), ('KPW', 'KPW'), ('UYI', 'UYI'), ('BAN', 'BAN'), ('SZL', 'SZL'), ('XBC', 'XBC'), ('JPY', 'JPY'), ('UGX', 'UGX'), ('FIM', 'FIM'), ('ARP', 'ARP'), ('SBD', 'SBD'), ('QAR', 'QAR'), ('BHD', 'BHD'), ('ILR', 'ILR'), ('BAM', 'BAM'), ('ERN', 'ERN'), ('ARM', 'ARM'), ('BOP', 'BOP'), ('ILP', 'ILP'), ('AZM', 'AZM'), ('XPF', 'XPF'), ('XPD', 'XPD'), ('LUC', 'LUC'), ('MAF', 'MAF'), ('MCF', 'MCF'), ('MVP', 'MVP'), ('VEF', 'VEF'), ('MNT', 'MNT'), ('KWD', 'KWD'), ('CHE', 'CHE'), ('AOA', 'AOA'), ('MRU', 'MRU'), ('HNL', 'HNL'), ('ISJ', 'ISJ'), ('GRD', 'GRD'), ('CZK', 'CZK'), ('BEL', 'BEL'), ('ZMK', 'ZMK'), ('PLZ', 'PLZ'), ('ZRZ', 'ZRZ'), ('SYP', 'SYP'), ('UAH', 'UAH'), ('GNF', 'GNF'), ('SKK', 'SKK'), ('YDD', 'YDD'), ('ZAR', 'ZAR'), ('JOD', 'JOD'), ('BRN', 'BRN'), ('GBP', 'GBP'), ('XAU', 'XAU'), ('XPT', 'XPT'), ('FKP', 'FKP'), ('XEU', 'XEU'), ('BWP', 'BWP'), ('XUA', 'XUA'), ('ECV', 'ECV'), ('SSP', 'SSP'), ('PHP', 'PHP'), ('CHF', 'CHF'), ('BGM', 'BGM'), ('XRE', 'XRE'), ('BBD', 'BBD'), ('YER', 'YER'), ('ISK', 'ISK'), ('BAD', 'BAD'), ('EUR', 'EUR'), ('NIO', 'NIO'), ('KGS', 'KGS'), ('BRR', 'BRR'), ('PEN', 'PEN'), ('BDT', 'BDT'), ('ZWL', 'ZWL'), ('GIP', 'GIP'), ('LYD', 'LYD'), ('SDD', 'SDD'), ('MDL', 'MDL'), ('ARL', 'ARL'), ('LRD', 'LRD'), ('XXX', 'XXX'), ('ZAL', 'ZAL'), ('CAD', 'CAD'), ('RWF', 'RWF'), ('MOP', 'MOP'), ('MZM', 'MZM'), ('BEC', 'BEC'), ('BOV', 'BOV'), ('DEM', 'DEM'), ('AZN', 'AZN'), ('NPR', 'NPR'), ('ZWD', 'ZWD'), ('MMK', 'MMK'), ('KYD', 'KYD'), ('GMD', 'GMD'), ('XSU', 'XSU'), ('NLG', 'NLG'), ('MKN', 'MKN'), ('MZN', 'MZN'), ('XBA', 'XBA'), ('ADP', 'ADP'), ('XFO', 'XFO'), ('SEK', 'SEK')], max_length=100),
        ),
    ]