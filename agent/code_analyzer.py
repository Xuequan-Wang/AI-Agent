import re
from typing import Dict, List


class CodeAnalyzer:
    MODULE_KEYWORDS = {
        "ADC": ["adc", "ADC", "analog", "采集", "模拟量"],
        "USART/UART": ["uart", "usart", "串口"],
        "Timer": ["timer", "定时器"],
        "GPIO": ["gpio"],
        "Sensor": ["温度", "传感器"],
    }

    def analyze(self, text: str) -> Dict[str, List[str]]:
        return {
            "headers": self._extract_headers(text),
            "functions": self._extract_functions(text),
            "modules": self._detect_modules(text),
        }

    def _extract_headers(self, text: str) -> List[str]:
        return re.findall(r'#include\\s*[<"]([^>"]+)[>"]', text)

    def _extract_functions(self, text: str) -> List[str]:
        return list(set(re.findall(r'\\b([a-zA-Z_][a-zA-Z0-9_]*)\\s*\\(', text)))[:10]

    def _detect_modules(self, text: str) -> List[str]:
        result = []
        for module, words in self.MODULE_KEYWORDS.items():
            for w in words:
                if w.lower() in text.lower():
                    result.append(module)
                    break
        return result
