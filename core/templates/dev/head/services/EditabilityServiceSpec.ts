// Copyright 2018 The Oppia Authors. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

/**
 * @fileoverview Unit tests for EditabilityService.
 */

import { EditabilityService } from 'services/EditabilityService.ts';

describe('EditabilityService', function() {
  let editabilityService: EditabilityService;

  beforeEach(() => {
    editabilityService = new EditabilityService();
  });

  it('should allow to edit an exploration after the tutorial ends', function() {
    editabilityService.onEndTutorial();
    editabilityService.markEditable();
    expect(editabilityService.isEditable()).toBe(true);
  });

  it('should allow to translate an exploration after the tutorial ends',
    function() {
      editabilityService.onEndTutorial();
      editabilityService.markTranslatable();
      expect(editabilityService.isTranslatable()).toBe(true);
    });

  it('should allow to edit an exploration outside the tutorial mode',
    function() {
      editabilityService.markEditable();
      expect(editabilityService.isEditableOutsideTutorialMode()).toBe(true);
    });

  it('should not allow to edit an exploration during tutorial mode',
    function() {
      editabilityService.onStartTutorial();
      expect(editabilityService.isEditable()).toBe(false);
    });

  it('should not allow to edit an uneditable exploration', function() {
    editabilityService.markNotEditable();
    expect(editabilityService.isEditable()).toBe(false);
  });
});
