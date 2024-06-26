from django.utils.translation import ugettext_lazy as _

EQUIPMENT_NOTICE_TYPES = (
    ('equipment-item-requires-moderation', _('A new equipment item requires moderation'), '', 2),
    ('equipment-item-approved', _('Equipment item you created was approved'), '', 2),
    ('equipment-item-assigned', _('Equipment item was assigned to you'), '', 2),
    ('equipment-item-rejected', _('Equipment item you created was rejected'), '', 2),
    ('equipment-item-rejected-affected-image', _('Rejected equipment item removed from your image'), '', 2),
    ('equipment-edit-proposal-created', _('Equipment item received an edit proposal'), '', 2),
    ('equipment-edit-proposal-approved', _('Your edit proposal was approved'), '', 2),
    ('equipment-edit-proposal-assigned', _('Edit proposal assigned to you'), '', 2),
    ('equipment-edit-proposal-rejected', _('Your edit proposal was rejected'), '', 2),
    ('equipment-item-migration-approved', _('Approved migration proposal of an equipment item'), '', 2),
    ('equipment-item-migration-rejected', _('Rejected migration proposal of an equipment item'), '', 2),
    ('ambiguous-item-removed-from-presets', _('Ambiguous equipment item removed from presets'), '', 2),
    ('new-image-from-followed-equipment', _('New image from followed equipment item'), '', 2),
    ('marketplace-offer-created', _('New offer for your marketplace listing'), '', 2),
    ('marketplace-offer-created-buyer', _('Your offer for a marketplace listing was recorded'), '', 2),
    ('marketplace-offer-updated', _('Offer for your marketplace listing got updated'), '', 2),
    ('marketplace-offer-updated-buyer', _('Your offer for a marketplace listing was updated'), '', 2),
    ('marketplace-offer-accepted-by-seller', _('Marketplace offer accepted by seller'), '', 2),
    ('marketplace-offer-accepted-by-you', _('Marketplace offer accepted by you'), '', 2),
    ('marketplace-offer-rejected-by-seller', _('Marketplace offer rejected by seller'), '', 2),
    ('marketplace-offer-retracted', _('Marketplace offer retracted by buyer'), '', 2),
    ('marketplace-offer-retracted-buyer', _('Marketplace offer retracted successfully'), '', 2),
    ('marketplace-listing-updated', _('Marketplace listing updated'), '', 2),
    ('marketplace-listing-deleted', _('Marketplace listing deleted'), '', 2),
    ('marketplace-listing-approved', _('Marketplace listing approved'), '', 2),
    ('marketplace-listing-expired', _('Marketplace listing expired'), '', 2),
    ('marketplace-listing-line-item-sold', _('Marketplace listing line item sold'), '', 2),
    ('marketplace-listing-by-user-you-follow', _('New marketplace listing by user you follow'), '', 2),
    ('marketplace-listing-for-item-you-follow', _('New marketplace listing for item you follow'), '', 2),
    ('marketplace-rate-seller', _('Rate the seller for your recent purchase'), '', 2),
    ('marketplace-rate-buyer', _('Rate the buyer for your recent sale'), '', 2),
    ('marketplace-mark-sold-reminder', _('Mark your listing as sold if needed'), '', 2),
    ('comment-to-marketplace-feedback-received', _('New comment to a marketplace feedback you received'), '', 2),
    ('comment-to-marketplace-feedback-left', _('New comment to a marketplace feedback you left'), '', 2),
)
