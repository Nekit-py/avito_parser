import json
import requests


abs = [('/sankt-peterburg/kvartiry/apartamenty-studiya_267_m_916_et._2295678059',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/svobodnogo_naznacheniya_25_m_2088795155',
  '/sankt-peterburg/kvartiry/1-k._kvartira_24_m_910_et._2234717001',
  '/sankt-peterburg/kvartiry/1-k._kvartira_351_m_126_et._1872354436',
  '/sankt-peterburg/kvartiry/1-k._kvartira_33m_45et._56075088',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofisnoe_torgovoe_1000_m_s_vidom_na_nevu_2285621984',
  '/sankt-peterburg/kvartiry/3-k._kvartira_582m_45et._2176537334',
  '/sankt-peterburg/kvartiry/1-k._apartamenty_483_m_415_et._2140935191',
  '/sankt-peterburg/kvartiry/2-k._kvartira_71_m_1417_et._2274706539',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/idealnye_mesto_dlya_vashego_biznesa_200_m_2142405673',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_140_m_open_space_2285669344',
  '/sankt-peterburg/kvartiry/2-k._kvartira_1134_m_78_et._2229361349',
  '/sankt-peterburg/kvartiry/2-k._kvartira_49m_34et._2261459498',
  '/sankt-peterburg/kvartiry/kvartira-studiya_254_m_718_et._2192448716',
  '/sankt-peterburg/kvartiry/1-k._kvartira_395_m_711_et._2293199492',
  '/sankt-peterburg/kvartiry/1-k._kvartira_364_m_2123_et._2096515589',
  '/sankt-peterburg/kvartiry/apartamenty-studiya_294m_46et._2321121069',
  '/sankt-peterburg/kvartiry/3-k._kvartira_1088_m_34_et._2005943341',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/skladpr-vo_1-yy_etazh_220_m_dostup_247parkovka_2315778986',
  '/sankt-peterburg/kvartiry/3-k._kvartira_1126_m_611_et._2084017634',
  '/sankt-peterburg/kvartiry/2-k._kvartira_652_m_1318_et._2263613859',
  '/sankt-peterburg/kvartiry/kvartira-studiya_22m_16et._2095436887',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_299_m_otdelnyy_blok_2253651705',
  '/sankt-peterburg/kvartiry/1-k._kvartira_548_m_1212_et._2272488651',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_vidovoy_1900_m_s_terrasoy_vid_na_nevu_2285801733',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_200_m_otdelnyy_blok_2253104967',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofisy_vidovye_980_m_do_1900_kvm_s_vidom_na_nevu_2284952783',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_vidovoy_1500_m_vid_na_nevu_2285074880',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/proizvodstvo_2500_m_mozhno_pischevoe_2285589261',
  '/sankt-peterburg/kvartiry/2-k._kvartira_765_m_1516_et._2263566709',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_loft_400_m_2285289100',
  '/sankt-peterburg/kvartiry/2-k._kvartira_847_m_618_et._2263550412',
  '/sankt-peterburg/kvartiry/1-k._kvartira_547_m_1111_et._2305782343',
  '/sankt-peterburg/kvartiry/3-k._kvartira_75m_24et._1402431865',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofisy_ot_16_m_do_211_kv_m_ot_sobstvennika_2314418782',
  '/sankt-peterburg/kvartiry/2-k._kvartira_45_m_411_et._2305272056',
  '/sankt-peterburg/kvartiry/3-k._kvartira_953_m_78_et._2249059529',
  '/sankt-peterburg/kvartiry/2-k._kvartira_681_m_718_et._2295671946',
  '/sankt-peterburg/kvartiry/3-k._kvartira_681_m_126_et._2096640844',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_s_konditsionerami_190m_2314365107',
  '/sankt-peterburg/kvartiry/kvartira-studiya_27m_2023et._2301120497',
  '/sankt-peterburg/kvartiry/kvartira-studiya_255_m_112_et._2293774621',
  '/sankt-peterburg/kvartiry/kvartira-studiya_238_m_1717_et._2261803585',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/sobstvennik_sdaet_ofis_43_m_1994039986',
  '/sankt-peterburg/kvartiry/1-k._kvartira_322_m_1012_et._2325423779',
  '/sankt-peterburg/kvartiry/kvartira-studiya_16m_15et._2331217043',
  '/sankt-peterburg/kvartiry/2-k._kvartira_487_m_1324_et._2293431718',
  '/sankt-peterburg/kvartiry/kvartira-studiya_244_m_89_et._2325675986',
  '/sankt-peterburg/kvartiry/1-k._kvartira_45_m_49_et._2260943043',
  '/sankt-peterburg/kvartiry/2-k._kvartira_488_m_712_et._2261619126',
  '/sankt-peterburg/kvartiry/kvartira-studiya_261_m_710_et._2325731086',
  '/sankt-peterburg/kvartiry/kvartira-studiya_247_m_314_et._2261635155',
  '/sankt-peterburg/kvartiry/3-k._kvartira_932_m_38_et._2229441048',
  '/sankt-peterburg/kvartiry/2-k._kvartira_486_m_424_et._2261578138',
  '/sankt-peterburg/kvartiry/2-k._kvartira_484_m_1224_et._2293044392',
  '/sankt-peterburg/kvartiry/1-k._kvartira_429_m_510_et._2293265152'),
 ('/sankt-peterburg/kvartiry/3-k._kvartira_781_m_710_et._2325213762',
  '/sankt-peterburg/kvartiry/2-k._kvartira_517_m_312_et._2229277992',
  '/sankt-peterburg/kvartiry/2-k._kvartira_483_m_424_et._2261533119',
  '/sankt-peterburg/kvartiry/1-k._kvartira_333_m_710_et._2261006439',
  '/sankt-peterburg/kvartiry/2-k._kvartira_598_m_710_et._2261397452',
  '/sankt-peterburg/kvartiry/1-k._kvartira_341_m_39_et._2325767343',
  '/sankt-peterburg/kvartiry/1-k._kvartira_459_m_512_et._2229256254',
  '/sankt-peterburg/kvartiry/2-k._kvartira_785_m_39_et._2249310985',
  '/sankt-peterburg/kvartiry/apartamenty-studiya_267_m_1116_et._2295158313',
  '/sankt-peterburg/kvartiry/1-k._kvartira_456_m_58_et._2096627445',
  '/sankt-peterburg/kvartiry/2-k._kvartira_704_m_28_et._2229286619',
  '/sankt-peterburg/kvartiry/kvartira-studiya_247_m_417_et._2261173358',
  '/sankt-peterburg/kvartiry/1-k._kvartira_311_m_317_et._2261412393',
  '/sankt-peterburg/kvartiry/1-k._kvartira_349_m_518_et._2192594622',
  '/sankt-peterburg/kvartiry/1-k._kvartira_355_m_124_et._2224264870',
  '/sankt-peterburg/kvartiry/kvartira-studiya_277_m_625_et._2190613085',
  '/sankt-peterburg/kvartiry/2-k._kvartira_525_m_312_et._2261539011',
  '/sankt-peterburg/kvartiry/1-k._kvartira_328_m_912_et._2293254386',
  '/sankt-peterburg/kvartiry/4-k._kvartira_971_m_710_et._2293725416',
  '/sankt-peterburg/kvartiry/kvartira-studiya_248_m_417_et._2261716144',
  '/sankt-peterburg/kvartiry/kvartira-studiya_246_m_212_et._2325564203',
  '/sankt-peterburg/kvartiry/kvartira-studiya_241_m_1416_et._2325468361',
  '/sankt-peterburg/kvartiry/kvartira-studiya_248_m_416_et._2261484746',
  '/sankt-peterburg/kvartiry/2-k._kvartira_569_m_813_et._2293804980',
  '/sankt-peterburg/kvartiry/3-k._kvartira_1049_m_99_et._2324899398',
  '/sankt-peterburg/kvartiry/3-k._kvartira_887_m_39_et._2324960396',
  '/sankt-peterburg/kvartiry/2-k._kvartira_616_m_413_et._2261303007',
  '/sankt-peterburg/kvartiry/kvartira-studiya_247_m_317_et._2261759175',
  '/sankt-peterburg/kvartiry/2-k._kvartira_613_m_610_et._2229434417',
  '/sankt-peterburg/kvartiry/2-k._kvartira_652_m_712_et._2325134245',
  '/sankt-peterburg/kvartiry/kvartira-studiya_248_m_416_et._2325761947',
  '/sankt-peterburg/kvartiry/2-k._kvartira_661_m_710_et._2325091446',
  '/sankt-peterburg/kvartiry/1-k._kvartira_454_m_29_et._2325290653',
  '/sankt-peterburg/kvartiry/1-k._kvartira_318_m_317_et._2324996796',
  '/sankt-peterburg/kvartiry/1-k._kvartira_388_m_610_et._2325251239',
  '/sankt-peterburg/kvartiry/1-k._kvartira_356_m_1624_et._2324973190',
  '/sankt-peterburg/kvartiry/1-k._kvartira_449_m_49_et._2325353745',
  '/sankt-peterburg/kvartiry/kvartira-studiya_24_m_314_et._2325319700',
  '/sankt-peterburg/kvartiry/1-k._kvartira_322_m_210_et._2325564652',
  '/sankt-peterburg/kvartiry/2-k._kvartira_723_m_712_et._2261586158',
  '/sankt-peterburg/kvartiry/2-k._kvartira_581_m_810_et._2325604476',
  '/sankt-peterburg/kvartiry/2-k._kvartira_79m_310et._2259339923',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/torgovaya_ploschad_55_m_2332628652',
  '/sankt-peterburg/kvartiry/2-k._kvartira_57m_35et._2306832987',
  '/sankt-peterburg/kvartiry/2-k._kvartira_65m_1721et._2314621226',
  '/sankt-peterburg/kvartiry/2-k._kvartira_635_m_1014_et._2260188669',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/svobodnogo_naznacheniya_50_m_2288338477',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/ofis_39.7_m_ot_sobstvennika_2058621525',
  '/sankt-peterburg/kvartiry/kvartira-studiya_11m_19et._1857259433',
  '/sankt-peterburg/kvartiry/3-k._kvartira_1344_m_69_et._2039323414',
  '/sankt-peterburg/kvartiry/2-k._kvartira_909_m_1819_et._2263177373',
  '/sankt-peterburg/kvartiry/2-k._kvartira_45m_610et._1471546744',
  '/sankt-peterburg/kvartiry/kvartira-studiya_12m_35et._1719508318',
  '/sankt-peterburg/kommercheskaya_nedvizhimost/svobodnogo_naznacheniya_61_m_2288285585',
  '/sankt-peterburg/kvartiry/1-k._kvartira_369_m_114_et._2100804123',
  '/sankt-peterburg/kvartiry/2-k._kvartira_679_m_511_et._2276452364')]


links = [''.join(('https://www.avito.ru', link)) for tup in abs for link in tup]


class ToManyRequests(BaseException):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f"Reuqests error: {self.message}"
        else:
            return "Нас немножко забанили)"


def get_html(url):
    response = requests.get(url)
    if response.status_code == 429:
        raise ToManyRequests
    else:
        return response.status_code


print(type(get_html(links[0])))




