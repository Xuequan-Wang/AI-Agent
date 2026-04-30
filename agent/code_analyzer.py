import re
from typing import Dict, List


class CodeAnalyzer:
    MODULE_KEYWORDS = {
        "ADC": ["adc", "analog", "采集", "模拟量"],
        "USART/UART": ["uart", "usart", "串口"],
        "Timer": ["timer", "tim", "定时器"],
        "GPIO": ["gpio", "引脚"],
        "PWM": ["pwm"],
        "I2C": ["i2c"],
        "SPI": ["spi"],
        "Sensor": ["温度", "湿度", "传感器", "sensor"],
        "Control": ["pid", "控制", "control"],
    }

    def analyze(self, text: str) -> Dict[str, List[str]]:
        text = text or ""
        return {
            "headers": self._extract_headers(text),
            "functions": self._extract_functions(text),
            "modules": self._detect_modules(text),
        }

    def _extract_headers(self, text: str) -> List[str]:
        pattern = r'#include\s*[<"]([^>"]+)[>"]'
        return sorted(set(re.findall(pattern, text)))

    def _extract_functions(self, text: str) -> List[str]:
        pattern = r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*\('
        ignored = {"if", "for", "while", "switch", "return", "sizeof"}
        functions = [name for name in re.findall(pattern, text) if name not in ignored]
        return sorted(set(functions))[:20]

    def _detect_modules(self, text: str) -> List[str]:
        result = []
        lower_text = text.lower()
        for module, words in self.MODULE_KEYWORDS.items():
            for word in words:
                if word.lower() in lower_text:
                    result.append(module)
                    break
        return result
