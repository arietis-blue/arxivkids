// https://vue-i18n.intlify.dev/guide/installation.html
import { createI18n } from 'vue-i18n'
import localEn from './languages/en'
import localJa from './languages/ja'
import localZhCn from './languages/zh-cn'

const i18n = createI18n({
    legacy: false,
    locale: 'ja',
    messages: {
        'en': localEn,
        'ja': localJa,
        'zh-cn': localZhCn
    }
})

export default i18n