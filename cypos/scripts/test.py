from base.models import Substitutes

s = Substitutes.objects.get(id=268)
print(s.courseSubOf)