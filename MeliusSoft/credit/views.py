from django.shortcuts import render
from django.views import View
from .models import Contract, CreditBit
from .forms import IdForm


class MyView(View):
    form = IdForm

    def post(self, request):
        form = IdForm(request.POST)
        context_dict = {'form': self.form}

        if form.is_valid():
            contract_id = form.cleaned_data.get("contract_id")
            creditbit = CreditBit.objects.filter(contract_id=contract_id).first()

            if not creditbit:
                return render(request, template_name="contract.html", context={'form': self.form})

            list_ids = list(creditbit.products.all().distinct()
                            .values_list("manufacturer__pk", flat=True))

            # Просто для души
            list_names = list(creditbit.products.all().distinct()
                              .values_list("manufacturer__name", flat=True))

            context_dict.update({'list_ids': list_ids, 'list_names': list_names})

        return render(request, template_name="contract.html", context=context_dict)

    def get(self, request):
        return render(request, template_name="contract.html", context={'form': self.form})
