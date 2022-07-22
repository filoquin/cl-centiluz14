##############################################################################
#
#    Copyright (C) 2021  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your optiogitn) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#   le agregamos esto
##############################################################################

{
    'name': 'centiluz14',
    'version': '14.0.1.0.0',
    'category': 'Tools',
    'summary': "Centiluz for v14 CE",
    'author': "jeo Software",
    'website': 'http://github.com/filoquin/cl-localizacion14',
    'license': 'AGPL-3',
    'depends': [
        'standard_depends_ce'
        ],
    'installable': True,

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # Config to write in odoo.conf
    'config': [

        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
                'workers = 5',
                'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
                'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
                'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
                'limit_memory_hard = 2684354560',
    ],

    'port': '8069',

    'git-repos': [
        'https://github.com/filoquin/cl-centiluz14.git',

        # OCA
        'https://github.com/OCA/server-tools oca-server-tools -b 14.0',
        'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow -b 14.0',
        'https://github.com/OCA/sale-workflow oca-sale-workflow -b 14.0',
        'https://github.com/OCA/field-service oca-field-service -b 14.0',
        'https://github.com/OCA/hr oca-hr -b 14.0',
        'https://github.com/OCA/social oca-social -b 14.0',
        'https://github.com/OCA/partner-contact oca-partner-contact -b 14.0',
        'https://github.com/OCA/pos oca-pos -b 14.0',
        'https://github.com/OCA/reporting-engine oca-reporting-engine -b 14.0',
        'https://github.com/OCA/hr-expense oca-hr-expense -b 14.0',
        'https://github.com/OCA/edi oca-edi -b 14.0',
        'https://github.com/OCA/manufacture oca-manufacture -b 14.0',
        'https://github.com/OCA/crm oca-crm -b 14.0',
        'https://github.com/OCA/purchase-workflow oca-purchase-workflow -b 14.0',
        'https://github.com/OCA/project oca-project -b 14.0',
        'https://github.com/OCA/search-engine oca-search-engine -b 14.0',
        'https://github.com/OCA/maintenance oca-maintenance -b 14.0',
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse -b 14.0',
        'https://github.com/OCA/account-payment oca-account-payment -b 14.0',
        'https://github.com/OCA/multi-company oca-multi-company -b 14.0',
        'https://github.com/OCA/rma oca-rma -b 14.0',
        'https://github.com/OCA/delivery-carrier oca-delivery-carrier -b 14.0',
        'https://github.com/OCA/operating-unit oca-operating-unit -b 14.0',
        'https://github.com/OCA/knowledge oca-knowledge -b 14.0',
        'https://github.com/OCA/wms oca-wms -b 14.0',
        'https://github.com/OCA/mis-builder oca-mis-builder -b 14.0',
        'https://github.com/OCA/bank-payment oca-bank-payment -b 14.0',
        'https://github.com/OCA/account-invoice-reporting oca-account-invoice-reporting -b 14.0',
        'https://github.com/OCA/timesheet oca-timesheet -b 14.0',
        'https://github.com/OCA/web oca-web -b 14.0',
        'https://github.com/OCA/account-financial-tools oca-account-financial-tools -b 14.0',
        'https://github.com/OCA/sale-reporting oca-sale-reporting -b 14.0',
        'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting -b 14.0',
        'https://github.com/OCA/e-commerce oca-e-commerce -b 14.0',
        'https://github.com/OCA/contract oca-contract -b 14.0',
        'https://github.com/OCA/helpdesk oca-helpdesk -b 14.0',
        'https://github.com/OCA/product-attribute oca-product-attribute -b 14.0',
        'https://github.com/OCA/account-analytic -b 14.0',
        'https://github.com/OCA/server-ux oca-server-ux -b 14.0',
        'https://github.com/OCA/website oca-website -b 14.0',
        'https://github.com/OCA/ddmrp oca-ddmrp -b 14.0',
        'https://github.com/OCA/account-fiscal-rule oca-account-fiscal-rule -b 14.0',
        'https://github.com/OCA/storage oca-storage -b 14.0',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting -b 14.0',
        'https://github.com/OCA/geospatial oca-geospatial -b 14.0',
        'https://github.com/OCA/vertical-hotel oca-vertical-hotel -b 14.0',
        'https://github.com/OCA/server-auth oca-server-auth -b 14.0',
        'https://github.com/OCA/account-reconcile oca-account-reconcile -b 14.0',
        'https://github.com/OCA/server-backend oca-server-backend -b 14.0',
        'https://github.com/OCA/vertical-association oca-vertical-association -b 14.0',
        'https://github.com/OCA/account-invoicing oca-account-invoicing -b 14.0',
        'https://github.com/OCA/product-variant oca-product-variant -b 14.0',
        'https://github.com/OCA/queue oca-queue -b 14.0',
        'https://github.com/OCA/account-closing oca-account-closing -b 14.0',
        'https://github.com/OCA/iot oca-iot -b 14.0',
        'https://github.com/OCA/dms oca-dms -b 14.0',
        'https://github.com/OCA/margin-analysis oca-margin-analysis -b 14.0',
        'https://github.com/OCA/payroll oca-payroll -b 14.0',
        'https://github.com/OCA/hr-holidays oca-hr-holidays -b 14.0',
        'https://github.com/OCA/role-policy oca-role-policy -b 14.0',
        'https://github.com/OCA/apps-store oca-apps-store -b 14.0',
        'https://github.com/OCA/rest-framework rest-framework -b 14.0',
        'https://github.com/OCA/brand rest-brand -b 14.0',
        'https://github.com/OCA/report-print-send oca-report-print-send -b 14.0',
        'https://github.com/OCA/server-brand oca-server-brand -b 14.0',
        'https://github.com/OCA/business-requirement oca-business-requirement -b 14.0',
        'https://github.com/OCA/commission oca-commission -b 14.0',
        'https://github.com/OCA/product-pack oca-product-pack -b 14.0',
        'https://github.com/OCA/currency oca-currency -b 14.0',
        'https://github.com/OCA/credit-control oca-credit-control -b 14.0',
        'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode -b 14.0',
        'https://github.com/OCA/event oca-event -b 14.0',
        'https://github.com/OCA/hr-attendance oca-hr-attendance -b 14.0',
        'https://github.com/OCA/website-cms oca-website-cms -b 14.0',
        'https://github.com/OCA/survey oca-survey -b 14.0',
        'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport -b 14.0',
        'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting -b 14.0',
        'https://github.com/OCA/management-system oca-management-system -b 14.0',
        'https://github.com/OCA/fleet oca-fleet -b 14.0',
        'https://github.com/OCA/project-reporting oca-project-reporting -b 14.0',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting -b 14.0',

        # ingadhoc
        #'https://github.com/ingadhoc/product ingadhoc-product -b 14.0',
        #'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous -b 14.0',
        #'https://github.com/ingadhoc/sale ingadhoc-sale -b 14.0',
        #'https://github.com/ingadhoc/purchase ingadhoc-purchase -b 14.0',
        #'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools -b 14.0',
        #'https://github.com/ingadhoc/website ingadhoc-website -b 14.0',
        #'https://github.com/ingadhoc/account-invoicing ingadhoc-account-invoicing -b 14.0',
        #'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports -b 14.0',
        #'https://github.com/ingadhoc/odoo-public-administration ingadhoc-odoo-public-administration -b 14.0',
        #'https://github.com/ingadhoc/account-payment ingadhoc-account-payment -b 14.0',
        #'https://github.com/ingadhoc/multi-company ingadhoc-multi-company -b 14.0',
        #'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale -b 14.0',
        #'https://github.com/ingadhoc/stock ingadhoc-stock -b 14.0',
        #'https://github.com/ingadhoc/partner ingadhoc-partner -b 14.0',
        #'https://github.com/ingadhoc/odoo-argentina-ce ingadhoc-odoo-argentina-ce -b 14.0',
        #'https://github.com/ingadhoc/multi-store ingadhoc-multi-store -b 14.0',

        # themes
        'https://github.com/odoo/design-themes.git odoo-themes -b 14.0',
        
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:14.0',
        'postgres postgres:10.1-alpine',
        #'nginx nginx'
    ]
}
