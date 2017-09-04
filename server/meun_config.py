# -*- coding: utf-8 -*-

menu_config = [
    {
        "name": "员工管理",
        "index": "1-0",
        "children": [
            {
                "index": "1-1",
                "name": "用户管理",
                'path': '/admin/user_manage'
            },
            {
                "index": "1-2",
                "name": "员工信息维护",
                'path': '/admin/emplyee_manage'
            }
        ]
    },
    {
        "name": "商家管理",
        "index": "2-0",
        "children": [
            {
                "index": "2-1",
                "name": "商家信息维护",
                "path": '/admin/carousel_manage'
            },
            {
                "index": '2-2',
                "name": "排选商家菜单",
                "path": '/admin/character_illustration_manage'
            }
        ]
    },
    {
        "name": "订单管理",
        "index": "3-0",
        "children": [
            {
                "index": '3-1',
                "name": '点餐下单',
                "path": '/admin/sms_reservation_log'
            },
            {
                "index": '3-2',
                "name": '点餐数据统计',
                "path": '/admin/award_config'
            },
            {
                "index": '3-3',
                "name": '月度点餐明细',
                "path": '/admin/award_draw_log'
            },
            {
                "index": '3-4',
                "name": '查询历史点餐',
                "path": '/admin/award_draw_log'
            }
        ]
    }
]
