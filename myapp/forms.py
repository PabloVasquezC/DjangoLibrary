from django import forms
from .models import MovimientoProducto, DetalleMovimiento, Producto

class DetalleMovimientoForm(forms.ModelForm):
    class Meta:
        model = DetalleMovimiento
        fields = ['producto', 'cantidad']

class MovimientoProductoForm(forms.ModelForm):
    detalles_movimiento = forms.Field(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = MovimientoProducto
        fields = ['bodega_origen', 'bodega_destino', 'usuario']

    def save(self, commit=True):
        instance = super().save(commit=False)
        detalles = self.cleaned_data.get('detalles_movimiento', [])
        instance.detalles_movimiento = detalles
        if commit:
            instance.save()
        return instance
