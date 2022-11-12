changes = [
    # flared_70
    [
        0x1ADF0 + 0x20,
        bytes.fromhex('000273020000060A06166F030000066F040000066F050000060B0728060000060C0828070000060D1A8D0800000225D009000004280A00000609280B000006130411040703280C0000061305110513062B0011062A'),
        [
            [0x00000003, 0x0A0000E5],
            [0x0000000B, 0x0A0000A3],
            [0x00000010, 0x0A0000A4],
            [0x00000015, 0x0A0000E6],
            [0x0000001C, 0x060000B3],
            [0x00000023, 0x060000B9],
            [0x0000002A, 0x0100002F],
            [0x00000030, 0x04000140],
            [0x00000035, 0x0A000092],
            [0x0000003B, 0x06000080],
            [0x00000046, 0x060000B5]
        ]
    ],
    # flared_66
    [
        0x19b90,
        bytes.fromhex('00D00200000228030000066F040000060A140B140C72050000700D7206000070130406026F0700000674080000020B076F090000060C280A000006076F0B000006130F120FFE160C0000026F0D0000066F0E0000061305280F000006076F100000066F110000066F1200000613062813000006076F1400000613101210FE16150000026F160000066F17000006130700076F1800000613111613122B2B111111129A131300110411136F19000006252D0426142B056F1A000006281B000006130400111217581312111211118E6932CD281C000006086F1D00000613141214281E0000066F1F0000061308086F200000068E692821000006130900086F220000066F2300000613152B2511156F240000061316000911166F25000006252D0426142B056F2600000628270000060D0011156F280000062DD2DE0D11152C0811156F2900000600DC282A000006096F2B000006130A282C00000611046F2D000006130B282E000006282F000006130C110C11096F3000000600110C11056F3100000600110C11066F3200000600110C11086F3300000600110C110A6F3400000600110C110B6F3500000600110C11076F3600000600110C6F37000006130D110D8E69185A7338000006130E1613172B21110E110D11178F39000002723A000070283B0000066F3C000006261117175813171117110D8E69FE04131811182DD1110E6F3D00000613192B0011192A'),
        [
            [0x00000002, 0x0200001C],
            [0x00000007, 0x0A00006C],
            [0x0000000C, 0x0A0000B3],
            [0x00000016, 0x70000011],
            [0x0000001C, 0x70000011],
            [0x00000025, 0x0A0000B4],
            [0x0000002A, 0x0100006C],
            [0x00000031, 0x0A0000B5],
            [0x00000037, 0x0A0000A5],
            [0x0000003D, 0x0A0000B6],
            [0x00000047, 0x0100006F],
            [0x0000004C, 0x0A000044],
            [0x00000051, 0x0A00009D],
            [0x00000058, 0x0A0000A5],
            [0x0000005E, 0x0A0000B7],
            [0x00000063, 0x0A000044],
            [0x00000068, 0x0A00009D],
            [0x0000006F, 0x0A0000A5],
            [0x00000075, 0x0A0000B8],
            [0x0000007F, 0x01000070],
            [0x00000084, 0x0A000044],
            [0x00000089, 0x0A00009D],
            [0x00000092, 0x0A0000B9],
            [0x000000AA, 0x0A0000BA],
            [0x000000B6, 0x0A000044],
            [0x000000BB, 0x0A000028],
            [0x000000D1, 0x0A0000A5],
            [0x000000D7, 0x0A0000BB],
            [0x000000E0, 0x0A00003B],
            [0x000000E5, 0x0A00009D],
            [0x000000ED, 0x0A0000BC],
            [0x000000F4, 0x0A0000BD],
            [0x000000FD, 0x0A0000BE],
            [0x00000102, 0x0A0000BF],
            [0x0000010D, 0x0A0000C0],
            [0x00000118, 0x0A0000C1],
            [0x00000124, 0x0A000044],
            [0x00000129, 0x0A000028],
            [0x00000132, 0x0A0000C2],
            [0x00000141, 0x0A000046],
            [0x00000148, 0x0A0000A5],
            [0x0000014E, 0x0A00009D],
            [0x00000155, 0x0A0000A5],
            [0x0000015C, 0x0A00009D],
            [0x00000163, 0x0A000081],
            [0x00000168, 0x0A000082],
            [0x00000173, 0x0A0000A6],
            [0x0000017D, 0x0A0000A6],
            [0x00000187, 0x0A0000A6],
            [0x00000191, 0x0A0000A6],
            [0x0000019B, 0x0A0000A6],
            [0x000001A5, 0x0A0000A6],
            [0x000001AF, 0x0A0000A6],
            [0x000001B7, 0x0A00008F],
            [0x000001C4, 0x0A0000C3],
            [0x000001D6, 0x0100002F],
            [0x000001DB, 0x70003050],
            [0x000001E0, 0x0A0000C4],
            [0x000001E5, 0x0A0000C5],
            [0x00000201, 0x0A000044],
        ]
    ],
    # flared_69
    [
        0x1ACEA + 0x10 - 2,
        bytes.fromhex('0028B1E9468A6F543E61640A73632E321E0B0628F8FDCD5A00140C06191773D233FD380D0000076F547F7CCE13041613052B5B11041105A305842F8A1306000211067BB3A5F3D773C571C9DE6FAC6E49B6130711072C300011067B2D513FC68D3965B7010C0911067B8732C8806E166FF39AC4812609081611067B708A8E856F32FE7F4B262B0F00110517581305110511048E69329D00DE0B092C07096FE407783F00DC0813082B0011082A'),
        [
            [0x00000002, 0x0A0000E3],
            [0x00000007, 0x0A00006B],
            [0x0000000D, 0x06000065],
            [0x00000014, 0x06000059],
            [0x0000001F, 0x0A000067],
            [0x00000028, 0x06000063],
            [0x00000038, 0x0200001A],
            [0x00000043, 0x040000DF],
            [0x00000048, 0x0A000017],
            [0x0000004D, 0x0A0000E4],
            [0x0000005B, 0x040000E0],
            [0x00000060, 0x0100002F],
            [0x00000069, 0x040000E3],
            [0x00000070, 0x0A000056],
            [0x0000007B, 0x040000E0],
            [0x00000080, 0x0A000057],
            [0x0000009E, 0x0A000046],
        ]
    ],
    # flared_35
    [
        0xABC0 + 0x2c,
        bytes.fromhex('0002191773772F0F9A0A000673D3E08ABF0B0728975D331F80988DBAB9067F8AB685257B482476526E166F35172CE426076F17B9C80D0C0728FAEE90098017FA23AF0728D9EF40EF80B63BD7AE7FDADB69917B1572C3FA8D889A8F6380CCB0195D160D2B17007E74BE0A02090728C42C1EF5A4D50B682C000917580D097EF4CC98BC8E69FE04130411042DD900DE0B062C07066F5118833600DC2A'),
        [
            [0x00000005, 0x0A000067],
            [0x0000000D, 0x0A000068],
            [0x00000014, 0x2B000007],
            [0x00000019, 0x04000057],
            [0x0000001F, 0x04000057],
            [0x00000024, 0x0400007A],
            [0x0000002B, 0x0A000056],
            [0x00000032, 0x0A000069],
            [0x00000039, 0x2B000008],
            [0x0000003E, 0x04000058],
            [0x00000044, 0x2B000009],
            [0x00000049, 0x04000059],
            [0x0000004E, 0x04000058],
            [0x00000053, 0x040000D9],
            [0x00000058, 0x0200001A],
            [0x0000005D, 0x0400005B],
            [0x00000067, 0x0400005B],
            [0x0000006E, 0x2B00000A],
            [0x00000073, 0x0200001A],
            [0x0000007E, 0x0400005B],
            [0x00000094, 0x0A000046],
        ]
    ],
    # flared_47
    [
        0xB580,
        bytes.fromhex('0020000100008D02000002130520000100008D030000021306038E698D040000021307160B2B16001105070207028E695D919E110607079E000717580B072000010000FE04130811082DDC16250B0C2B2C00081106079458110507945820000100005D0C110607941304110607110608949E11060811049E000717580B072000010000FE04130911092DC616250B250C0A2B52000617580A0620000100005D0A0811060694580C0820000100005D0C110606941304110606110608949E11060811049E110611060694110608945820000100005D940D1107070307910961D29C000717580B07038E69FE04130A110A2DA21107130B2B00110B2A'),
        [
            [0x00000007, 0x0100003A],
            [0x00000013, 0x0100003A],
            [0x0000001D, 0x0100002F]
        ]
    ],
    # flared_67
    [
        0x19E0C,
        bytes.fromhex('007302000006251F58166F03000006002520D6000000166F04000006002520D7000000166F0500000600251F5F166F0600000600252000FE0000166F0700000600251F3B196F0800000600251F2E186F0900000600251F3C196F0A00000600251F2F186F0B00000600251F41196F0C00000600251F34186F0D00000600251F3D196F0E00000600251F30186F0F00000600251F42196F1000000600251F35186F1100000600251F3E196F1200000600251F31186F1300000600251F43196F1400000600251F36186F1500000600251F3F196F1600000600251F32186F1700000600251F44196F1800000600251F37186F1900000600251F40196F1A00000600251F33186F1B0000060025208C000000176F1C00000600251F38196F1D00000600251F2B186F1E000006002517166F1F00000600251F39196F2000000600251F2C186F2100000600251F3A196F2200000600251F2D186F2300000600251F28176F2400000600251F29176F2500000600251F6F176F2600000600251F74176F2700000600252001FE0000166F2800000600252002FE0000166F2900000600252003FE0000166F2A000006002520C3000000166F2B00000600252004FE0000166F2C00000600252005FE0000166F2D00000600252016FE0000176F2E000006002520D3000000166F2F00000600251F67166F3000000600251F68166F3100000600251F69166F3200000600251F6A166F33000006002520D4000000166F340000060025208A000000166F35000006002520B3000000166F3600000600252082000000166F37000006002520B5000000166F3800000600252083000000166F39000006002520B7000000166F3A00000600252084000000166F3B000006002520B9000000166F3C00000600252085000000166F3D000006002520D5000000166F3E0000060025208B000000166F3F000006002520B4000000166F4000000600252086000000166F41000006002520B6000000166F4200000600252087000000166F43000006002520B8000000166F4400000600252088000000166F45000006002520BA000000166F4600000600252089000000166F4700000600251F76166F4800000600251F6B166F4900000600251F6C166F4A000006002520E0000000166F4B000006002520D2000000166F4C000006002520D1000000166F4D00000600251F6D166F4E00000600251F6E166F4F00000600252017FE0000166F5000000600251F70176F5100000600251F5B166F5200000600251F5C166F5300000600251F25166F5400000600252011FE0000166F55000006002520DC000000166F5600000600252018FE0000166F5700000600252015FE0000176F5800000600251F75176F5900000600251F27176F5A00000600252009FE00001B6F5B000006002518166F5C000006002519166F5D00000600251A166F5E00000600251B166F5F00000600251F0E1A6F600000060025200AFE00001B6F6100000600251F0F1A6F6200000600251F201C6F6300000600251F16166F6400000600251F17166F6500000600251F18166F6600000600251F19166F6700000600251F1A166F6800000600251F1B166F6900000600251F1C166F6A00000600251F1D166F6B00000600251F1E166F6C00000600251F15166F6D00000600251F1F1A6F6E00000600251F211D6F6F00000600251F221C6F7000000600251F231D6F71000006002520A3000000176F7200000600252097000000166F7300000600252090000000166F7400000600252092000000166F7500000600252094000000166F7600000600252096000000166F7700000600252098000000166F7800000600252099000000166F790000060025209A000000166F7A00000600252091000000166F7B00000600252093000000166F7C00000600252095000000166F7D0000060025208F000000176F7E00000600251F7B176F7F00000600251F7C176F8000000600252006FE0000176F8100000600251F4D166F8200000600251F46166F8300000600251F48166F8400000600251F4A166F8500000600251F4C166F8600000600251F4E166F8700000600251F4F166F8800000600251F50166F8900000600251F47166F8A00000600251F49166F8B00000600251F4B166F8C0000060025208E000000166F8D0000060025200CFE00001B6F8E00000600251C166F8F00000600251D166F9000000600251E166F9100000600251F09166F9200000600251F111A6F930000060025200DFE00001B6F9400000600251F121A6F9500000600251F14166F9600000600251F71176F9700000600251F7E176F9800000600251F7F176F9900000600251F72176F9A000006002520D0000000176F9B00000600252007FE0000176F9C000006002520DD000000196F9D000006002520DE000000186F9E0000060025200FFE0000166F9F000006002520C6000000176FA000000600251F5A166FA1000006002520D8000000166FA2000006002520D9000000166FA300000600251F65166FA40000060025208D000000176FA500000600251F73176FA600000600252019FE00001A6FA7000006002516166FA800000600251F66166FA900000600251F60166FAA00000600251F26166FAB000006002520FE000000166FAC000006002520FD000000166FAD000006002520FC000000166FAE000006002520FB000000166FAF000006002520FA000000166FB0000006002520F9000000166FB1000006002520F8000000166FB2000006002520FF000000166FB30000060025201EFE0000166FB40000060025201DFE0000166FB5000006002520C2000000176FB600000600251F5D166FB700000600251F5E166FB800000600251F2A166FB90000060025201AFE0000166FBA00000600251F62166FBB00000600251F63166FBC00000600251F64166FBD0000060025201CFE0000176FBE0000060025200BFE00001B6FBF00000600251F101A6FC0000006002520A4000000176FC10000060025209B000000166FC20000060025209C000000166FC30000060025209D000000166FC40000060025209E000000166FC50000060025209F000000166FC6000006002520A0000000166FC7000006002520A1000000166FC8000006002520A2000000166FC900000600251F7D176FCA000006002520DF000000166FCB00000600251F52166FCC00000600251F53166FCD00000600251F54166FCE00000600251F55166FCF00000600251F56166FD000000600251F57166FD100000600251F51166FD20000060025200EFE00001B6FD300000600251F0A166FD400000600251F0B166FD500000600251F0C166FD600000600251F0D166FD700000600251F131A6FD800000600252081000000176FD900000600252080000000176FDA00000600251F59166FDB000006002520DA000000166FDC000006002520DB000000166FDD00000600251F451E6FDE00000600252014FE0000166FDF00000600251F7A166FE000000600252012FE00001A6FE100000600251F79176FE2000006002520A5000000176FE300000600252013FE0000166FE400000600251F61166FE5000006000A160B160C160DD0E600000228E70000066FE800000613041104036FE90000061305110574EA000002130611066FEB000006130711078E698DEC000002130828ED000006130916130F2B17001108110F1107110F9A6FEE000006A200110F1758130F110F11088E69FE04131011102DDB11056FEF000006130A72F000007011066FF10000061108110A1773F2000006130B110B6FF3000006130C11066FF4000006130D00110D6FF50000066FF600000613112B1A11116FF7000006131200110911126FF80000066FF9000006000011116FFA0000062DDDDE0D11112C0811116FFB00000600DC11096FFC000006130E110C110E6FFD00000600161313389E020000000211139120FE000000FE01131511152C17002000FE0000021113175891580B111317581313002B0700021113910B0006076FFE00000613141113175813131114131711171316111645090000001B000000410000000500000010000000050000002302000010000000200000002B0000003826020000111317581313381B02000011131A5813133810020000380B02000011131E581313380002000011131A02111328FF0000061A5A5858131338EA01000002111328000100060C0820BDA698A2610C082000000070370A0820FFFF0070FE052B0116131811182C1700110C1104086F010100066F020100060D0038730100000011066F03010006131914131A14131B11196F040100062D0911196F050100062B0117131D111D2C0911196F06010006131A11066F070100062D0911066F080100062B0117131E111E2C0911066F09010006131B11196F0A01000608111A111B6F0B010006131C111C6F0C0100066F0D010006720E010070280F010006131F111F2C3100110C111C74100100026F11010006111C74120100026F1301000674140100026F150100066F160100060D0038BE000000111C6F170100066F180100067219010070281A010006132011202C1B00110C111C741B0100026F1C0100066F1D0100060D003887000000111C6F1E010006721F01007028200100062D13111C6F21010006722201007028230100062B0117132111212C2E00110C111C74240100026F25010006111C74260100026F2701000674280100026F290100066F2A0100060D002B2C00110C111C742B0100026F2C010006111C742D0100026F2E010006742F0100026F300100066F310100060D000002111309D29C0211131758091E63D29C0211131858091F1063D29C0211131958091F1863D29C11131A5813132B081113185813132B00001113028E69FE04132211223A52FDFFFF110C02110D6F320100066F3301000600110B14046F3401000613232B0011232A'),
        [
            [0x00000002, 0x0A0000C6],
            [0x0000000B, 0x0A0000C7],
            [0x00000018, 0x0A0000C7],
            [0x00000025, 0x0A0000C7],
            [0x0000002F, 0x0A0000C7],
            [0x0000003C, 0x0A0000C7],
            [0x00000046, 0x0A0000C7],
            [0x00000050, 0x0A0000C7],
            [0x0000005A, 0x0A0000C7],
            [0x00000064, 0x0A0000C7],
            [0x0000006E, 0x0A0000C7],
            [0x00000078, 0x0A0000C7],
            [0x00000082, 0x0A0000C7],
            [0x0000008C, 0x0A0000C7],
            [0x00000096, 0x0A0000C7],
            [0x000000A0, 0x0A0000C7],
            [0x000000AA, 0x0A0000C7],
            [0x000000B4, 0x0A0000C7],
            [0x000000BE, 0x0A0000C7],
            [0x000000C8, 0x0A0000C7],
            [0x000000D2, 0x0A0000C7],
            [0x000000DC, 0x0A0000C7],
            [0x000000E6, 0x0A0000C7],
            [0x000000F0, 0x0A0000C7],
            [0x000000FA, 0x0A0000C7],
            [0x00000104, 0x0A0000C7],
            [0x00000111, 0x0A0000C7],
            [0x0000011B, 0x0A0000C7],
            [0x00000125, 0x0A0000C7],
            [0x0000012E, 0x0A0000C7],
            [0x00000138, 0x0A0000C7],
            [0x00000142, 0x0A0000C7],
            [0x0000014C, 0x0A0000C7],
            [0x00000156, 0x0A0000C7],
            [0x00000160, 0x0A0000C7],
            [0x0000016A, 0x0A0000C7],
            [0x00000174, 0x0A0000C7],
            [0x0000017E, 0x0A0000C7],
            [0x0000018B, 0x0A0000C7],
            [0x00000198, 0x0A0000C7],
            [0x000001A5, 0x0A0000C7],
            [0x000001B2, 0x0A0000C7],
            [0x000001BF, 0x0A0000C7],
            [0x000001CC, 0x0A0000C7],
            [0x000001D9, 0x0A0000C7],
            [0x000001E6, 0x0A0000C7],
            [0x000001F0, 0x0A0000C7],
            [0x000001FA, 0x0A0000C7],
            [0x00000204, 0x0A0000C7],
            [0x0000020E, 0x0A0000C7],
            [0x0000021B, 0x0A0000C7],
            [0x00000228, 0x0A0000C7],
            [0x00000235, 0x0A0000C7],
            [0x00000242, 0x0A0000C7],
            [0x0000024F, 0x0A0000C7],
            [0x0000025C, 0x0A0000C7],
            [0x00000269, 0x0A0000C7],
            [0x00000276, 0x0A0000C7],
            [0x00000283, 0x0A0000C7],
            [0x00000290, 0x0A0000C7],
            [0x0000029D, 0x0A0000C7],
            [0x000002AA, 0x0A0000C7],
            [0x000002B7, 0x0A0000C7],
            [0x000002C4, 0x0A0000C7],
            [0x000002D1, 0x0A0000C7],
            [0x000002DE, 0x0A0000C7],
            [0x000002EB, 0x0A0000C7],
            [0x000002F8, 0x0A0000C7],
            [0x00000305, 0x0A0000C7],
            [0x00000312, 0x0A0000C7],
            [0x0000031C, 0x0A0000C7],
            [0x00000326, 0x0A0000C7],
            [0x00000330, 0x0A0000C7],
            [0x0000033D, 0x0A0000C7],
            [0x0000034A, 0x0A0000C7],
            [0x00000357, 0x0A0000C7],
            [0x00000361, 0x0A0000C7],
            [0x0000036B, 0x0A0000C7],
            [0x00000378, 0x0A0000C7],
            [0x00000382, 0x0A0000C7],
            [0x0000038C, 0x0A0000C7],
            [0x00000396, 0x0A0000C7],
            [0x000003A0, 0x0A0000C7],
            [0x000003AD, 0x0A0000C7],
            [0x000003BA, 0x0A0000C7],
            [0x000003C7, 0x0A0000C7],
            [0x000003D4, 0x0A0000C7],
            [0x000003DE, 0x0A0000C7],
            [0x000003E8, 0x0A0000C7],
            [0x000003F5, 0x0A0000C7],
            [0x000003FE, 0x0A0000C7],
            [0x00000407, 0x0A0000C7],
            [0x00000410, 0x0A0000C7],
            [0x00000419, 0x0A0000C7],
            [0x00000423, 0x0A0000C7],
            [0x00000430, 0x0A0000C7],
            [0x0000043A, 0x0A0000C7],
            [0x00000444, 0x0A0000C7],
            [0x0000044E, 0x0A0000C7],
            [0x00000458, 0x0A0000C7],
            [0x00000462, 0x0A0000C7],
            [0x0000046C, 0x0A0000C7],
            [0x00000476, 0x0A0000C7],
            [0x00000480, 0x0A0000C7],
            [0x0000048A, 0x0A0000C7],
            [0x00000494, 0x0A0000C7],
            [0x0000049E, 0x0A0000C7],
            [0x000004A8, 0x0A0000C7],
            [0x000004B2, 0x0A0000C7],
            [0x000004BC, 0x0A0000C7],
            [0x000004C6, 0x0A0000C7],
            [0x000004D0, 0x0A0000C7],
            [0x000004DD, 0x0A0000C7],
            [0x000004EA, 0x0A0000C7],
            [0x000004F7, 0x0A0000C7],
            [0x00000504, 0x0A0000C7],
            [0x00000511, 0x0A0000C7],
            [0x0000051E, 0x0A0000C7],
            [0x0000052B, 0x0A0000C7],
            [0x00000538, 0x0A0000C7],
            [0x00000545, 0x0A0000C7],
            [0x00000552, 0x0A0000C7],
            [0x0000055F, 0x0A0000C7],
            [0x0000056C, 0x0A0000C7],
            [0x00000579, 0x0A0000C7],
            [0x00000583, 0x0A0000C7],
            [0x0000058D, 0x0A0000C7],
            [0x0000059A, 0x0A0000C7],
            [0x000005A4, 0x0A0000C7],
            [0x000005AE, 0x0A0000C7],
            [0x000005B8, 0x0A0000C7],
            [0x000005C2, 0x0A0000C7],
            [0x000005CC, 0x0A0000C7],
            [0x000005D6, 0x0A0000C7],
            [0x000005E0, 0x0A0000C7],
            [0x000005EA, 0x0A0000C7],
            [0x000005F4, 0x0A0000C7],
            [0x000005FE, 0x0A0000C7],
            [0x00000608, 0x0A0000C7],
            [0x00000615, 0x0A0000C7],
            [0x00000622, 0x0A0000C7],
            [0x0000062B, 0x0A0000C7],
            [0x00000634, 0x0A0000C7],
            [0x0000063D, 0x0A0000C7],
            [0x00000647, 0x0A0000C7],
            [0x00000651, 0x0A0000C7],
            [0x0000065E, 0x0A0000C7],
            [0x00000668, 0x0A0000C7],
            [0x00000672, 0x0A0000C7],
            [0x0000067C, 0x0A0000C7],
            [0x00000686, 0x0A0000C7],
            [0x00000690, 0x0A0000C7],
            [0x0000069A, 0x0A0000C7],
            [0x000006A7, 0x0A0000C7],
            [0x000006B4, 0x0A0000C7],
            [0x000006C1, 0x0A0000C7],
            [0x000006CE, 0x0A0000C7],
            [0x000006DB, 0x0A0000C7],
            [0x000006E8, 0x0A0000C7],
            [0x000006F2, 0x0A0000C7],
            [0x000006FF, 0x0A0000C7],
            [0x0000070C, 0x0A0000C7],
            [0x00000716, 0x0A0000C7],
            [0x00000723, 0x0A0000C7],
            [0x0000072D, 0x0A0000C7],
            [0x0000073A, 0x0A0000C7],
            [0x00000743, 0x0A0000C7],
            [0x0000074D, 0x0A0000C7],
            [0x00000757, 0x0A0000C7],
            [0x00000761, 0x0A0000C7],
            [0x0000076E, 0x0A0000C7],
            [0x0000077B, 0x0A0000C7],
            [0x00000788, 0x0A0000C7],
            [0x00000795, 0x0A0000C7],
            [0x000007A2, 0x0A0000C7],
            [0x000007AF, 0x0A0000C7],
            [0x000007BC, 0x0A0000C7],
            [0x000007C9, 0x0A0000C7],
            [0x000007D6, 0x0A0000C7],
            [0x000007E3, 0x0A0000C7],
            [0x000007F0, 0x0A0000C7],
            [0x000007FA, 0x0A0000C7],
            [0x00000804, 0x0A0000C7],
            [0x0000080E, 0x0A0000C7],
            [0x0000081B, 0x0A0000C7],
            [0x00000825, 0x0A0000C7],
            [0x0000082F, 0x0A0000C7],
            [0x00000839, 0x0A0000C7],
            [0x00000846, 0x0A0000C7],
            [0x00000853, 0x0A0000C7],
            [0x0000085D, 0x0A0000C7],
            [0x0000086A, 0x0A0000C7],
            [0x00000877, 0x0A0000C7],
            [0x00000884, 0x0A0000C7],
            [0x00000891, 0x0A0000C7],
            [0x0000089E, 0x0A0000C7],
            [0x000008AB, 0x0A0000C7],
            [0x000008B8, 0x0A0000C7],
            [0x000008C5, 0x0A0000C7],
            [0x000008D2, 0x0A0000C7],
            [0x000008DC, 0x0A0000C7],
            [0x000008E9, 0x0A0000C7],
            [0x000008F3, 0x0A0000C7],
            [0x000008FD, 0x0A0000C7],
            [0x00000907, 0x0A0000C7],
            [0x00000911, 0x0A0000C7],
            [0x0000091B, 0x0A0000C7],
            [0x00000925, 0x0A0000C7],
            [0x0000092F, 0x0A0000C7],
            [0x0000093C, 0x0A0000C7],
            [0x00000946, 0x0A0000C7],
            [0x00000950, 0x0A0000C7],
            [0x0000095A, 0x0A0000C7],
            [0x00000964, 0x0A0000C7],
            [0x0000096E, 0x0A0000C7],
            [0x0000097B, 0x0A0000C7],
            [0x00000988, 0x0A0000C7],
            [0x00000992, 0x0A0000C7],
            [0x0000099F, 0x0A0000C7],
            [0x000009AC, 0x0A0000C7],
            [0x000009B6, 0x0A0000C7],
            [0x000009C3, 0x0A0000C7],
            [0x000009CD, 0x0A0000C7],
            [0x000009DA, 0x0A0000C7],
            [0x000009E4, 0x0A0000C7],
            [0x000009F1, 0x0A0000C7],
            [0x000009FE, 0x0A0000C7],
            [0x00000A08, 0x0A0000C7],
            [0x00000A15, 0x0200001C],
            [0x00000A1A, 0x0A00006C],
            [0x00000A1F, 0x0A0000B3],
            [0x00000A29, 0x0A0000B4],
            [0x00000A32, 0x0100006C],
            [0x00000A3B, 0x0A0000B9],
            [0x00000A46, 0x01000052],
            [0x00000A4D, 0x0A0000C8],
            [0x00000A63, 0x0A0000BA],
            [0x00000A80, 0x0A0000C9],
            [0x00000A87, 0x70000011],
            [0x00000A8E, 0x0A0000B7],
            [0x00000A98, 0x0A0000CA],
            [0x00000AA1, 0x0A0000CB],
            [0x00000AAA, 0x0A0000B5],
            [0x00000AB4, 0x0A0000BE],
            [0x00000AB9, 0x0A0000BF],
            [0x00000AC4, 0x0A0000C0],
            [0x00000AD0, 0x0A0000C1],
            [0x00000AD5, 0x0A0000CC],
            [0x00000ADE, 0x0A0000C2],
            [0x00000AED, 0x0A000046],
            [0x00000AF6, 0x0A0000CD],
            [0x00000B01, 0x0A0000CE],
            [0x00000B41, 0x0A0000CF],
            [0x00000BB2, 0x060000B7],
            [0x00000BC5, 0x060000B7],
            [0x00000BF2, 0x0A0000D0],
            [0x00000BF7, 0x0A0000D1],
            [0x00000C06, 0x0A0000C9],
            [0x00000C15, 0x0A0000D2],
            [0x00000C1E, 0x0A0000D3],
            [0x00000C2E, 0x0A0000D4],
            [0x00000C37, 0x0A0000D5],
            [0x00000C40, 0x0A0000D6],
            [0x00000C50, 0x0A0000D7],
            [0x00000C59, 0x0A0000B3],
            [0x00000C63, 0x0A0000D8],
            [0x00000C6C, 0x0A0000D9],
            [0x00000C71, 0x0A0000DA],
            [0x00000C76, 0x70003056],
            [0x00000C7B, 0x0A00004A],
            [0x00000C8B, 0x0100007A],
            [0x00000C90, 0x0A0000DB],
            [0x00000C97, 0x0100007A],
            [0x00000C9C, 0x0A0000C9],
            [0x00000CA1, 0x0100007B],
            [0x00000CA6, 0x0A0000DC],
            [0x00000CAB, 0x0A0000DD],
            [0x00000CB9, 0x0A0000D9],
            [0x00000CBE, 0x0A0000DA],
            [0x00000CC3, 0x7000306E],
            [0x00000CC8, 0x0A00004A],
            [0x00000CD8, 0x0100007B],
            [0x00000CDD, 0x0A0000DC],
            [0x00000CE2, 0x0A0000DE],
            [0x00000CF0, 0x0A0000DA],
            [0x00000CF5, 0x70003086],
            [0x00000CFA, 0x0A00004A],
            [0x00000D03, 0x0A0000DA],
            [0x00000D08, 0x70003092],
            [0x00000D0D, 0x0A00004A],
            [0x00000D20, 0x0100007C],
            [0x00000D25, 0x0A0000DF],
            [0x00000D2C, 0x0100007C],
            [0x00000D31, 0x0A0000C9],
            [0x00000D36, 0x0100007B],
            [0x00000D3B, 0x0A0000DC],
            [0x00000D40, 0x0A0000E0],
            [0x00000D4E, 0x0100006C],
            [0x00000D53, 0x0A0000DF],
            [0x00000D5A, 0x0100006C],
            [0x00000D5F, 0x0A0000C9],
            [0x00000D64, 0x0100007B],
            [0x00000D69, 0x0A0000DC],
            [0x00000D6E, 0x0A0000E0],
            [0x00000DC2, 0x0A0000BB],
            [0x00000DC7, 0x0A0000E1],
            [0x00000DD1, 0x0A0000E2],
        ]
    ],
    # flared_68
    [
        0x1AC5C,
        bytes.fromhex('00160A020319589120000000015A0A06020318589120000001005A580A06020317589120000100005A580A06020391580A060B2B00072A'),
        []
    ],
]

with open("FlareOn.Backdoor.exe", 'rb') as f:
    data = f.read()

data = bytearray(data)
for address, value, tokens in changes:
    data[address:address + len(value)] = value
    for offset, token in tokens:
        data[address + offset: address + offset + 4] = token.to_bytes(4, 'little')

with open("FlareOn.Backdoor.deobfus.exe", 'wb') as f:
    f.write(data)