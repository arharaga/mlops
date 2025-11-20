# Отображаемый лимит памяти - 16ГБ
c.ResourceUseDisplay.mem_limit = 17179869184
# На последних 10% памяти подсвечивать красным
c.ResourceUseDisplay.mem_warning_threshold=0.1

# Прибивать ядра не активные последние 3 дня
c.MappingKernelManager.cull_idle_timeout = 60 * 60 * 24 * 3
# Проверять ядра каждый час
c.MappingKernelManager.cull_interval = 60 * 60