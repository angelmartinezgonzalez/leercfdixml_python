import os
from xml.etree import ElementTree as ET


def iniciApp(message):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Mensaje , {message}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    iniciApp('iniciando app lee datos del cfdi')
    file_xml =  '83425872.xml'
    file_xml_path = os.path.join(os.path.dirname(__file__), file_xml)
    print(file_xml_path)

    try:
        root = ET.parse(file_xml_path).getroot()
    except Exception as e:
        print(file_xml_path)
        print(e)

    Version = root.attrib['Version']
    Serie = root.attrib['Serie']
    Folio = root.attrib['Folio']
    Fecha = root.attrib['Fecha']
    Sello = root.attrib['Sello']
    FormaPago = root.attrib['FormaPago']
    NoCertificado = root.attrib['NoCertificado']
    CondicionesDePago = root.attrib['CondicionesDePago']
    SubTotal = root.attrib['SubTotal']
    Moneda = root.attrib['Moneda']
    Total = root.attrib['Total']
    TipoDeComprobante = root.attrib['TipoDeComprobante']
    Exportacion = root.attrib['Exportacion']
    MetodoPago = root.attrib['MetodoPago']
    LugarExpedicion = root.attrib['LugarExpedicion']

    print(Version)
    print(Serie)
    print(Folio)
    print(Fecha)
    print(Sello)
    print(FormaPago)
    print(NoCertificado)
    print(CondicionesDePago)
    print(SubTotal)
    print(Moneda)
    print(Total)
    print(TipoDeComprobante)
    print(Exportacion)
    print(MetodoPago)
    print(LugarExpedicion)

    for child in root:
        print(child.tag, child.attrib)

    node = root.find('{http://www.sat.gob.mx/cfd/4}Emisor')
    print('nodo Emisor')
    print(node)
    if node is not None:
        print('nodo Emisor')
        print(node.attrib.items())
        emisorRfc = node.attrib['Rfc']
        emisorNombre = node.attrib['Nombre']
        emisorRegimenFiscal = node.attrib['RegimenFiscal']
    print('Valores del Emisor')
    print('emisorRfc', emisorRfc)
    print('emisorNombre', emisorNombre)
    print('emisorRegimenFiscal', emisorRegimenFiscal)



    node = root.find('{http://www.sat.gob.mx/cfd/4}Receptor')
    print('nodo Receptor')
    print(node)
    if node is not None:
        print('nodo Receptor')
        print(node.attrib.items())
        receptorRfc = node.attrib['Rfc']
        receptorNombre = node.attrib['Nombre']
        receptorDomicilioFiscalReceptor = node.attrib['DomicilioFiscalReceptor']
        receptorRegimenFiscalReceptor = node.attrib['RegimenFiscalReceptor']
        receptorUsoCFDI = node.attrib['UsoCFDI']

    print('Valores del Receptor')
    print('receptorRfc', emisorRfc)
    print('receptorNombre', receptorNombre)
    print('receptorDomicilioFiscalReceptor', receptorDomicilioFiscalReceptor)
    print('receptorRegimenFiscalReceptor', receptorRegimenFiscalReceptor)
    print('receptorUsoCFDI', receptorUsoCFDI)

    node = root.find('{http://www.sat.gob.mx/cfd/4}Conceptos')
    print('nodo conceptos')
    print(node)
    if node is not None:
        print('nodo conceptos atributos')
        print(node.attrib.items())
        print('node Conceptos tag attrib')
        print(node.tag, node.attrib)

        for n in list(node):
            conceptoClaveProdServ = n.attrib.get('ClaveProdServ', '')
            conceptoCantidad = n.attrib.get('Cantidad', '')
            conceptoClaveUnidad = n.attrib.get('ClaveUnidad', '')
            conceptoUnidad = n.attrib['Unidad']
            conceptoDescripcion = n.attrib['Descripcion']
            conceptoValorUnitario = n.attrib['ValorUnitario']
            conceptoImporte = n.attrib['Importe']
            conceptoObjetoImp = n.attrib['ObjetoImp']

            print('valores del concepto')
            print('conceptoClaveProdServ', conceptoClaveProdServ)
            print('conceptoCantidad', conceptoCantidad)
            print('conceptoClaveUnidad', conceptoClaveUnidad)
            print('conceptoUnidad', conceptoUnidad)
            print('conceptoDescripcion', conceptoDescripcion)
            print('conceptoValorUnitario', conceptoValorUnitario)
            print('conceptoImporte', conceptoImporte)
            print('conceptoObjetoImp', conceptoObjetoImp)

            print('===========================')
            print('node de conceptos/concepto/Impuestos')
            for impuestos in n:
                print(impuestos.tag)
                print('node de conceptos/concepto/Impuestos/Traslados')
                for impuesto in impuestos:
                    print(impuesto.tag)
                    for impuestoTraslado in impuesto:
                        print('node de conceptos/concepto/Impuestos/Traslados/Traslado')
                        print(impuestoTraslado.tag)
                        if impuestoTraslado.tag == '{http://www.sat.gob.mx/cfd/4}Traslado':
                            conceptosConcepImpTrasTrasladoBase = impuestoTraslado.attrib.get('Base', '')
                            conceptosConcepImpTrasTrasladoImpuesto = impuestoTraslado.attrib.get('Impuesto', '')
                            conceptosConcepImpTrasTrasladoTipoFactor = impuestoTraslado.attrib.get('TipoFactor', '')
                            conceptosConcepImpTrasTrasladoTasaOCuota = impuestoTraslado.attrib.get('TasaOCuota', '')
                            conceptosConcepImpTrasTrasladoImporte = impuestoTraslado.attrib.get('Importe', '')
                            print('conceptosConcepImpTrasTrasladoBase ' + conceptosConcepImpTrasTrasladoBase)
                            print('conceptosConcepImpTrasTrasladoImpuesto ' + conceptosConcepImpTrasTrasladoImpuesto)
                            print('conceptosConcepImpTrasTrasladoTipoFactor ' + conceptosConcepImpTrasTrasladoTipoFactor)
                            print('conceptosConcepImpTrasTrasladoTasaOCuota ' +conceptosConcepImpTrasTrasladoTasaOCuota)
                            print('conceptosConcepImpTrasTrasladoImporte ' + conceptosConcepImpTrasTrasladoImporte)

            print('===========================')

    node = root.find('{http://www.sat.gob.mx/cfd/4}Impuestos')
    print('nodo Impuestos')
    print(node)
    if node is not None:
        print('nodo Impuestos atributos')
        print(node.attrib.items())
        print('node Impuestos tag attrib')
        print(node.tag, node.attrib)

        print('----' + node.attrib.get('TotalImpuestosTrasladados', '') )
        impuestosTotalImpuestosTrasladados = node.attrib.get('TotalImpuestosTrasladados', '')
        print('impuestosTotalImpuestosTrasladados ' + impuestosTotalImpuestosTrasladados)

        print('node.tag')
        print(node.tag)


        imp = node.find('{http://www.sat.gob.mx/cfd/4}Traslados' )
        if imp is not None:
            print('no vacio')
            for n in list(imp):
                impuestosTrasladosTraslado_Base = n.attrib['Base']
                impuestosTrasladosTraslado_Impuesto = n.attrib['Impuesto']
                impuestosTrasladosTraslado_TipoFactor = n.attrib['TipoFactor']
                impuestosTrasladosTraslado_TasaOCuota = n.attrib['TasaOCuota']
                impuestosTrasladosTraslado_Importe =n.attrib['Importe']
                print('impuestosTrasladosTraslado_Base ' + impuestosTrasladosTraslado_Base)
                print('impuestosTrasladosTraslado_Impuesto ' + impuestosTrasladosTraslado_Impuesto)
                print('impuestosTrasladosTraslado_TipoFactor ' + impuestosTrasladosTraslado_TipoFactor)
                print('impuestosTrasladosTraslado_TasaOCuota ' + impuestosTrasladosTraslado_TasaOCuota)
                print('impuestosTrasladosTraslado_Importe ' + impuestosTrasladosTraslado_Importe)

        imp = node.find('{http://www.sat.gob.mx/cfd/4}Retenciones')
        if imp is not None:
            for n in list(imp):
                retencionImpuesto = n.attrib['Impuesto']
                print('retencionImpuesto ' + retencionImpuesto)


    # Timbre
    node = root.find('{http://www.sat.gob.mx/cfd/4}Complemento/{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital')

    if node is not None:
        print(node.attrib['UUID'].upper())
        print(node.attrib['FechaTimbrado'].replace('T', ' ') )

    # Timbre2 otra forma de acceder
    node = root.find('{http://www.sat.gob.mx/cfd/4}Complemento')
    if node is not None:
        print('Aqui ')

        for n in list(node):
            print('complemento 2 node.tag')
            #{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital
            print(n.tag)
            print('UUID ' + n.attrib['UUID'].upper())
            print('Fecha de timbrado ' + n.attrib['FechaTimbrado'].replace('T', ' ') )



    # Timbre3 otra forma de acceder
    node = root.find('{http://www.sat.gob.mx/cfd/4}Complemento')
    if node is not None:
        print('Aqui 3 ')

        for n in list(node):
            print('complemento node.tag 3')
            #   {http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital
            print(n.tag)
            print('validamos que el tag corresponda a el timbre fiscal digital ')
            if n.tag == '{http://www.sat.gob.mx/TimbreFiscalDigital}TimbreFiscalDigital':
                print('UUID 3 ' + n.attrib['UUID'].upper())
                print('Fecha de timbrado  3 ' + n.attrib['FechaTimbrado'].replace('T', ' ') )

