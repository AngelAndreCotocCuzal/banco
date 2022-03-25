import json


class Prestamo:
    SCHEMA = {
        'code_prestamo': {
            'required': True,
            'type': 'string',
            'minlength': 1,
            'maxlength': 8
        },
        'code_asociado': {
            'required': True,
            'type': 'string',
            'minlength': 1,
            'maxlength': 8
        },
        'monto_solicitado': {
            'required': True,
            'type': 'string',
        },
        'monto_aprobado': {
            'type': 'string'
        },
        'numero_cuotas': {
            'type': 'integer',
            'minlength': 1,
            'maxlength': 50
        },
        'ingreso_mensual': {
            'required': True,
            'type': 'string',
        },
        'garantia': {
            'required': True,
            'type': 'string'
        },
        'plan_pagos': {
            'type': 'string'
        },
        'estado_prestamo': {
            'type': 'string'
        }
    }

    def _init_(self, code_prestamo: str, code_asociado: str, monto_solicitado: str, monto_aprobado: str,
                 numero_cuotas: int, ingreso_mensual: str, garantia: str, plan_pagos: str,
                 estado_prestamo: str) -> None:
        self._code_prestamo = code_prestamo
        self._code_asociado = code_asociado
        self._monto_solicitado = monto_solicitado
        self._monto_aprobado = monto_aprobado
        self._numero_cuotas = numero_cuotas
        self._ingreso_mensual = ingreso_mensual
        self._garantia = garantia
        self._plan_pagos = plan_pagos
        self._estado_prestamo = estado_prestamo
        self._errors = {}
 @property
    def errors(self) -> dict:
        return self._errors

    def create(self) -> bool:
        if self.is_valid():
            file = open('data.json')
            data = json.load(file)
            data['prestamos'].append({
                'code_prestamo': self._code_prestamo,
                'code_asociado': self._code_asociado,
                'monto_solicitado': self._monto_solicitado,
                'monto_aprobado': self._monto_aprobado,
                'numero_cuotas': self._numero_cuotas,
                'ingreso_mensual': self._ingreso_mensual,
                'garantia': self._garantia,
                'plan_pagos': self._plan_pagos,
                'estado_prestamo': self._estado_prestamo
            })
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
            file.close()
            return True
        else:
            return False
 def _iter_(self):
        yield 'code_prestamo', self._code_prestamo
        yield 'code_asociado', self._code_asociado
        yield 'monto_solicitado', self._monto_solicitado
        yield 'monto_aprobado', self._monto_aprobado
        yield 'numero_cuotas', self._numero_cuotas
        yield 'ingreso_mensual', self._ingreso_mensual
        yield 'garantia', self._garantia
        yield 'plan_pagos', self._plan_pagos
        yield 'estado_prestamo', self._estado_prestamo